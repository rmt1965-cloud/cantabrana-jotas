/**
 * CANTABRANA · RETAZOS DE VIDA — Recolector de estadísticas (Google Apps Script)
 * ---------------------------------------------------------------------------
 * Recibe eventos anónimos desde la web (POST) y los guarda en la hoja "Eventos".
 * Sirve los datos al panel de estadísticas (GET) SOLO si se aporta la clave.
 *
 * Instalación: ver INSTRUCCIONES_ESTADISTICAS.md
 */

// 1) CAMBIA ESTA CLAVE (solo la sabrás tú) y ejecuta la función  configurar()  una vez.
var CLAVE_INICIAL = 'CAMBIA-ESTA-CLAVE';

var HOJA = 'Eventos';
var COLS = ['Fecha (UTC)', 'Tipo', 'Jota', 'Sesion', 'Visitante', 'Dispositivo', 'Navegador', 'Pantalla', 'Idioma', 'Origen', 'Valor', 'Detalle'];
var TIPOS = ['visita', 'inicio', 'jota_play', 'jota_fin', 'valoracion', 'error', 'bloqueo', 'compartir'];
var MAX_FILAS_RESPUESTA = 60000;

// ---- CARGA Y SATURACIÓN (ajusta estos valores a tu criterio) ----
var CAPACIDAD_SIMULTANEA = 200;   // personas activas a la vez (ventana de los últimos 5 min) que consideras el 100 %
var UMBRAL_AVISO = 0.85;          // a partir del 85 % se avisa al visitante de que espere unos minutos
var CUOTA_MENSUAL_GB = 100;       // límite orientativo de GitHub Pages por mes
var MB_POR_VISITA = 12;           // peso medio estimado de una visita completa (audio, fotos, vídeo)

/** Ejecutar UNA vez desde el editor: crea la hoja y guarda la clave. */
function configurar() {
  if (!CLAVE_INICIAL || CLAVE_INICIAL === 'CAMBIA-ESTA-CLAVE' || CLAVE_INICIAL.length < 10) {
    throw new Error('Cambia CLAVE_INICIAL por una clave tuya de al menos 10 caracteres y vuelve a ejecutar.');
  }
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(HOJA) || ss.insertSheet(HOJA);
  if (sh.getLastRow() === 0) {
    sh.getRange(1, 1, 1, COLS.length).setValues([COLS]).setFontWeight('bold').setBackground('#c8922a').setFontColor('#ffffff');
    sh.setFrozenRows(1);
  }
  sh.getRange('A:L').setNumberFormat('@'); // todo como texto: evita que Sheets convierta fechas o fórmulas
  PropertiesService.getScriptProperties().setProperty('CLAVE', CLAVE_INICIAL);
  Logger.log('Listo. Hoja "' + HOJA + '" preparada y clave guardada. Ahora: Implementar > Nueva implementación > Aplicación web.');
}

// ------------------------------------------------------------------ ESCRITURA
function doPost(e) {
  try {
    var raw = (e && e.postData && e.postData.contents) || '';
    if (raw.length > 4000) return bloquear_('payload_enorme', '', raw.length + ' bytes');
    var d;
    try { d = JSON.parse(raw); } catch (x) { return bloquear_('payload_invalido', '', raw.slice(0, 80)); }
    if (!d || typeof d !== 'object') return bloquear_('payload_invalido', '', '');
    if (d.h) return bloquear_('honeypot', d.s, 'campo trampa relleno'); // campo que un humano nunca rellena
    var tipo = String(d.t || '');
    if (TIPOS.indexOf(tipo) < 0) return bloquear_('tipo_desconocido', d.s, tipo.slice(0, 40));

    var sid = limpiar_(d.s, 24);
    // Límite de frecuencia: máx. 40 eventos por sesión y minuto
    var cache = CacheService.getScriptCache();
    var kr = 'r_' + sid, n = parseInt(cache.get(kr) || '0', 10) + 1;
    cache.put(kr, String(n), 60);
    if (n > 40) { if (n === 41) bloquear_('flood', sid, 'más de 40 eventos/min'); return ok_(); }

    var valor = limpiar_(d.x, 200), detalle = limpiar_(d.y, 500), jota = limpiar_(d.j, 120);

    if (tipo === 'valoracion') {
      var nota = parseInt(valor, 10);
      if (!(nota >= 1 && nota <= 5)) return bloquear_('valoracion_invalida', sid, valor);
      if (cache.get('v_' + sid)) return bloquear_('valoracion_duplicada', sid, '');
      cache.put('v_' + sid, '1', 3600);
      valor = String(nota);
    }
    // Defensa contra inyección de fórmulas / HTML en comentarios y textos
    var t1 = neutralizar_(valor), t2 = neutralizar_(detalle);
    if (t1.alerta || t2.alerta) bloquear_(t1.alerta || t2.alerta, sid, (valor + ' ' + detalle).slice(0, 120), true);
    if (tipo !== 'bloqueo') marcarActivo_(sid, tipo);
    registrar_([new Date().toISOString(), tipo, jota, sid, limpiar_(d.v, 24), limpiar_(d.d, 20), limpiar_(d.n, 20),
      limpiar_(d.p, 12), limpiar_(d.l, 6), limpiar_(d.o, 80), t1.texto, t2.texto]);
    return ok_();
  } catch (err) {
    return ok_(); // nunca devolver errores internos
  }
}

// ------------------------------------------------------------------ LECTURA (panel)
function doGet(e) {
  var p = (e && e.parameter) || {};
  if (p.accion === 'ping') return json_({ ok: true });
  if (p.accion === 'estado') { var e_ = estado_(); return json_({ ok: true, nivel: e_.nivel, pct: e_.pct }); }
  if (p.accion !== 'datos') return json_({ ok: false, error: 'sin_accion' });

  var cache = CacheService.getScriptCache();
  var fallos = parseInt(cache.get('fallos') || '0', 10);
  if (fallos >= 8) return json_({ ok: false, error: 'bloqueado' }); // 8 claves erróneas = 15 min de bloqueo

  var clave = PropertiesService.getScriptProperties().getProperty('CLAVE') || '';
  if (!clave || !igual_(String(p.clave || ''), clave)) {
    cache.put('fallos', String(fallos + 1), 900);
    registrar_([new Date().toISOString(), 'bloqueo', '', '', '', '', '', '', '', '', 'clave_incorrecta', 'intento de acceso al panel (' + (fallos + 1) + ')']);
    return json_({ ok: false, error: 'clave' });
  }
  cache.remove('fallos');

  var desde = String(p.desde || '0000'), hasta = String(p.hasta || '9999');
  var sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(HOJA);
  var out = [];
  if (sh && sh.getLastRow() > 1) {
    var fin = sh.getLastRow(), bloque = 5000;
    while (fin > 1 && out.length < MAX_FILAS_RESPUESTA) {
      var ini = Math.max(2, fin - bloque + 1);
      var vals = sh.getRange(ini, 1, fin - ini + 1, COLS.length).getValues();
      var masAntiguo = false;
      for (var i = vals.length - 1; i >= 0; i--) {
        var f = String(vals[i][0]);
        if (f < desde) { masAntiguo = true; continue; }
        if (f <= hasta) out.push(vals[i].map(String));
      }
      if (masAntiguo) break;
      fin = ini - 1;
    }
  }
  out.reverse();
  return json_({ ok: true, cols: COLS, filas: out, truncado: out.length >= MAX_FILAS_RESPUESTA, carga: estado_() });
}

// ------------------------------------------------------------------ CARGA
// Personas activas = sesiones distintas con algún evento en los últimos 5 minutos (se guardan por minuto en la caché).
function marcarActivo_(sid, tipo) {
  try {
    var cache = CacheService.getScriptCache(), min = Math.floor(Date.now() / 60000), k = 'sm_' + min;
    var lock = LockService.getScriptLock();
    lock.waitLock(5000);
    try {
      var arr = JSON.parse(cache.get(k) || '[]');
      if (arr.indexOf(sid) < 0 && arr.length < 5000) { arr.push(sid); cache.put(k, JSON.stringify(arr), 600); }
      if (tipo === 'visita') {
        var props = PropertiesService.getScriptProperties(), mk = 'VM_' + new Date().toISOString().slice(0, 7);
        props.setProperty(mk, String((parseInt(props.getProperty(mk) || '0', 10)) + 1));
      }
    } finally { lock.releaseLock(); }
  } catch (e) {}
}
function estado_() {
  var cache = CacheService.getScriptCache(), c = cache.get('estado');
  if (c) { try { return JSON.parse(c); } catch (e) {} }
  var props = PropertiesService.getScriptProperties();
  var min = Math.floor(Date.now() / 60000), vistos = {}, n = 0;
  for (var i = 0; i < 5; i++) {
    try { JSON.parse(cache.get('sm_' + (min - i)) || '[]').forEach(function (s) { if (!vistos[s]) { vistos[s] = 1; n++; } }); } catch (e) {}
  }
  var pct = Math.round(100 * n / CAPACIDAD_SIMULTANEA);
  var visMes = parseInt(props.getProperty('VM_' + new Date().toISOString().slice(0, 7)) || '0', 10);
  var gb = visMes * MB_POR_VISITA / 1024;
  var forzado = props.getProperty('AVISO_FORZADO') === '1';
  var nivel = forzado || pct >= UMBRAL_AVISO * 100 ? 'saturado' : pct >= 60 ? 'alto' : 'ok';
  var r = { nivel: nivel, forzado: forzado, activos: n, capacidad: CAPACIDAD_SIMULTANEA, pct: pct,
    mes: { visitas: visMes, gb: Math.round(gb * 10) / 10, cuota: CUOTA_MENSUAL_GB, pct: Math.round(100 * gb / CUOTA_MENSUAL_GB) } };
  cache.put('estado', JSON.stringify(r), 20);
  return r;
}
/** Interruptor manual: ejecuta estas funciones desde el editor para mostrar / quitar el aviso a todos los visitantes. */
function activarAviso() { PropertiesService.getScriptProperties().setProperty('AVISO_FORZADO', '1'); CacheService.getScriptCache().remove('estado'); }
function desactivarAviso() { PropertiesService.getScriptProperties().deleteProperty('AVISO_FORZADO'); CacheService.getScriptCache().remove('estado'); }

// ------------------------------------------------------------------ utilidades
function ok_() { return ContentService.createTextOutput('ok'); }
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function limpiar_(v, max) { return String(v == null ? '' : v).replace(/[\u0000-\u001f]/g, ' ').slice(0, max); }
function igual_(a, b) { if (a.length !== b.length) return false; var r = 0; for (var i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i); return r === 0; }

function neutralizar_(t) {
  var alerta = '';
  if (/<\s*\/?\s*(script|iframe|img|svg|object|embed|link|style|on\w+\s*=)/i.test(t) || /javascript:/i.test(t)) { alerta = 'html_bloqueado'; t = t.replace(/[<>]/g, ''); }
  if (/^[=+\-@\t\r]/.test(t) && !/^-?\d+([.,]\d+)?$/.test(t)) { alerta = alerta || 'formula_bloqueada'; t = "'" + t; }
  return { texto: t, alerta: alerta };
}

function registrar_(fila) {
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(HOJA);
    if (!sh) { configurar_silencioso_(); sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(HOJA); }
    var r = sh.getLastRow() + 1;
    sh.getRange(r, 1, 1, fila.length).setNumberFormat('@').setValues([fila]);
  } finally { lock.releaseLock(); }
}
function configurar_silencioso_() {
  var sh = SpreadsheetApp.getActiveSpreadsheet().insertSheet(HOJA);
  sh.getRange(1, 1, 1, COLS.length).setValues([COLS]).setFontWeight('bold');
  sh.setFrozenRows(1);
}
function bloquear_(motivo, sid, detalle, noRespuesta) {
  try {
    registrar_([new Date().toISOString(), 'bloqueo', '', limpiar_(sid, 24), '', '', '', '', '', '', motivo, limpiar_(detalle, 200)]);
  } catch (e) {}
  return noRespuesta ? null : ok_();
}
