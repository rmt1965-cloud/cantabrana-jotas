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
    if (enListaNegra_(sid)) return ok_(); // sesión vetada por el vigilante: se ignora en silencio
    // Límite de frecuencia: máx. 40 eventos por sesión y minuto (15 si el escudo automático está activo)
    var cache = CacheService.getScriptCache();
    var lim = escudoActivo_() ? 15 : 40;
    var kr = 'r_' + sid, n = parseInt(cache.get(kr) || '0', 10) + 1;
    cache.put(kr, String(n), 60);
    if (n > lim) { if (n === lim + 1) bloquear_('flood', sid, 'más de ' + lim + ' eventos/min'); return ok_(); }

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
  return json_({ ok: true, cols: COLS, filas: out, truncado: out.length >= MAX_FILAS_RESPUESTA, carga: estado_(), seguridad: seguridad_() });
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

// ------------------------------------------------------------------ VIGILANTE (seguridad activa y automática)
// Se ejecuta solo cada hora (disparador). Revisa los eventos de las últimas 24 h y:
//  1) veta sesiones que acumulan bloqueos (24 h; el doble, el cuádruple... si reinciden; se olvidan solas a los 30 días)
//  2) aprende el nivel normal de ruido (media móvil) y activa un ESCUDO de 1 h (límites más estrictos) si hay un pico anormal
//  3) te envía un correo si hay pico, intentos de entrar al panel o cuota mensual alta (máx. 1 aviso del mismo tipo cada 6 h)
//  4) los lunes por la mañana te envía un resumen semanal
// Para ponerlo en marcha: ejecuta UNA vez  activarVigilancia()  desde el editor (pedirá permiso para enviar correos).
var VIG_BLOQUEOS_POR_SESION = 5;   // bloqueos en 24 h para vetar una sesión
var VIG_UMBRAL_MIN = 15;           // pico mínimo de bloqueos/hora para considerarlo anómalo
var VIG_FACTOR_PICO = 4;           // o 4 veces el nivel normal aprendido, lo que sea mayor
var VIG_CLAVE_MALA_AVISO = 5;      // intentos de clave errónea en 1 h que provocan aviso

function activarVigilancia() {
  desactivarVigilancia();
  ScriptApp.newTrigger('vigilar').timeBased().everyHours(1).create();
  vigilar();
  Logger.log('Vigilancia activa: se ejecuta cada hora. Los avisos llegarán a ' + correo_());
}
function desactivarVigilancia() {
  ScriptApp.getProjectTriggers().forEach(function (t) { if (t.getHandlerFunction() === 'vigilar') ScriptApp.deleteTrigger(t); });
}
function correo_() { try { return Session.getEffectiveUser().getEmail(); } catch (e) { return ''; } }

function leerDesde_(isoDesde) {
  var sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(HOJA), out = [];
  if (!sh || sh.getLastRow() < 2) return out;
  var fin = sh.getLastRow(), bloque = 3000;
  while (fin > 1 && out.length < 50000) {
    var ini = Math.max(2, fin - bloque + 1), vals = sh.getRange(ini, 1, fin - ini + 1, COLS.length).getValues(), viejo = false;
    for (var i = vals.length - 1; i >= 0; i--) { var f = String(vals[i][0]); if (f < isoDesde) { viejo = true; continue; } out.push(vals[i].map(String)); }
    if (viejo) break;
    fin = ini - 1;
  }
  return out;
}

function leerLista_() {
  var props = PropertiesService.getScriptProperties();
  try { return JSON.parse(props.getProperty('LISTA_NEGRA') || '{}'); } catch (e) { return {}; }
}
function enListaNegra_(sid) {
  if (!sid) return false;
  var cache = CacheService.getScriptCache(), l;
  try { l = JSON.parse(cache.get('ln') || 'null'); } catch (e) { l = null; }
  if (!l) { l = leerLista_(); try { cache.put('ln', JSON.stringify(l), 600); } catch (e) {} }
  return !!(l[sid] && l[sid].h > Date.now());
}
function escudoActivo_() {
  var cache = CacheService.getScriptCache(), c = cache.get('esc');
  if (c !== null) return c === '1';
  var h = parseInt(PropertiesService.getScriptProperties().getProperty('ESCUDO_HASTA') || '0', 10), on = h > Date.now();
  cache.put('esc', on ? '1' : '0', 60);
  return on;
}
function avisar_(tipo, asunto, cuerpo) {
  try {
    var props = PropertiesService.getScriptProperties(), k = 'AV_' + tipo, ult = parseInt(props.getProperty(k) || '0', 10);
    var espera = tipo === 'semanal' ? 6 * 864e5 : 6 * 36e5;
    if (Date.now() - ult < espera) return;
    var to = correo_(); if (!to) return;
    MailApp.sendEmail(to, '[Cantabrana] ' + asunto, cuerpo);
    props.setProperty(k, String(Date.now()));
  } catch (e) {}
}

function vigilar() {
  var props = PropertiesService.getScriptProperties(), cache = CacheService.getScriptCache(), ahora = Date.now();
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(20000)) return;
  try {
    var filas = leerDesde_(new Date(ahora - 24 * 36e5).toISOString()), h1 = new Date(ahora - 36e5).toISOString();
    var porSid = {}, motivos = {}, bl1h = 0, claveMala = 0;
    filas.forEach(function (f) {
      if (f[1] !== 'bloqueo') return;
      var m = f[10]; motivos[m] = (motivos[m] || 0) + 1;
      if (f[0] >= h1) { bl1h++; if (m === 'clave_incorrecta') claveMala++; }
      if (f[3] && m !== 'clave_incorrecta') porSid[f[3]] = (porSid[f[3]] || 0) + 1;
    });

    // 1) lista negra con caducidad progresiva
    var lista = leerLista_(), nuevos = 0;
    Object.keys(porSid).forEach(function (s) {
      if (porSid[s] < VIG_BLOQUEOS_POR_SESION) return;
      var e = lista[s];
      if (e && e.h > ahora) return;
      var n = (e ? e.n : 0) + 1;
      lista[s] = { h: ahora + Math.min(30, Math.pow(2, n - 1)) * 864e5, n: n };
      nuevos++;
    });
    Object.keys(lista).forEach(function (s) { if (lista[s].h < ahora - 30 * 864e5) delete lista[s]; });
    var claves = Object.keys(lista);
    if (claves.length > 150) { claves.sort(function (a, b) { return lista[b].h - lista[a].h; }).slice(150).forEach(function (s) { delete lista[s]; }); }
    props.setProperty('LISTA_NEGRA', JSON.stringify(lista)); cache.remove('ln');

    // 2) nivel normal aprendido y escudo temporal
    var base = parseFloat(props.getProperty('BASE_BL') || '0');
    var umbral = Math.max(VIG_UMBRAL_MIN, VIG_FACTOR_PICO * base), pico = bl1h > umbral;
    if (!pico) props.setProperty('BASE_BL', String(Math.round((0.9 * base + 0.1 * bl1h) * 100) / 100)); // solo aprende de horas normales
    if (pico) { props.setProperty('ESCUDO_HASTA', String(ahora + 36e5)); cache.remove('esc'); }

    // 3) avisos por correo
    var res = Object.keys(motivos).map(function (m) { return ' - ' + m + ': ' + motivos[m]; }).join('\n') || ' (ninguno)';
    if (pico) avisar_('pico', 'Pico de amenazas bloqueadas', 'En la última hora se han bloqueado ' + bl1h + ' intentos (lo normal ronda ' + Math.round(base) + ').\nEl escudo automático se ha activado durante 1 hora (límites más estrictos). No tienes que hacer nada.\n\nÚltimas 24 h:\n' + res);
    if (claveMala >= VIG_CLAVE_MALA_AVISO) avisar_('clave', 'Intentos de entrar al panel con clave errónea', 'Se han registrado ' + claveMala + ' intentos con clave errónea en la última hora. Si no has sido tú, cambia la clave del panel (ejecuta configurar con una clave nueva).');
    var est = estado_();
    if (est.mes && est.mes.pct >= 80) avisar_('cuota', 'Cuota mensual de visitas alta', 'Se estima que llevas el ' + est.mes.pct + ' % de la cuota mensual orientativa de GitHub Pages (' + est.mes.gb + ' de ' + est.mes.cuota + ' GB).');

    // 4) resumen semanal (lunes, a primera hora)
    var d = new Date();
    if (d.getDay() === 1 && d.getHours() >= 8 && d.getHours() <= 10) {
      var sem = leerDesde_(new Date(ahora - 7 * 864e5).toISOString()), c = { visita: 0, jota_play: 0, error: 0, bloqueo: 0 }, sum = 0, nv = 0;
      sem.forEach(function (f) { if (c[f[1]] !== undefined) c[f[1]]++; if (f[1] === 'valoracion') { var v = parseInt(f[10], 10); if (v >= 1 && v <= 5) { sum += v; nv++; } } });
      avisar_('semanal', 'Resumen semanal', 'Últimos 7 días:\n - Visitas: ' + c.visita + '\n - Jotas escuchadas: ' + c.jota_play + '\n - Valoraciones: ' + nv + (nv ? ' (media ' + (sum / nv).toFixed(1) + '/5)' : '') + '\n - Errores: ' + c.error + '\n - Amenazas bloqueadas: ' + c.bloqueo + '\n\nPanel: https://rmt1965-cloud.github.io/cantabrana-jotas/estadisticas.html');
    }
    props.setProperty('VIG_ULTIMA', new Date().toISOString());
    props.setProperty('VIG_RESUMEN', JSON.stringify({ bl1h: bl1h, bl24: filas.filter(function (f) { return f[1] === 'bloqueo'; }).length, nuevos: nuevos, vetadas: Object.keys(lista).filter(function (s) { return lista[s].h > ahora; }).length, base: base, umbral: Math.round(umbral) }));
  } finally { lock.releaseLock(); }
}
function seguridad_() {
  var p = PropertiesService.getScriptProperties(), r = {};
  try { r = JSON.parse(p.getProperty('VIG_RESUMEN') || '{}'); } catch (e) {}
  r.ultima = p.getProperty('VIG_ULTIMA') || ''; r.escudo = escudoActivo_();
  r.activo = ScriptApp.getProjectTriggers().some(function (t) { return t.getHandlerFunction() === 'vigilar'; });
  return r;
}

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
