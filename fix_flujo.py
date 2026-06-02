c = open('index.html', 'r', encoding='utf-8').read()

# 1. Quitar onclick del pergamino
c = c.replace(
    '<div class="perg-outer" id="perg-outer" onclick="iniciarJota()">',
    '<div class="perg-outer" id="perg-outer">'
)

# 2. Quitar texto "toca para escuchar"
c = c.replace(
    '\n      <div class="toca">&#10022; Toca para escuchar &#10022;</div>',
    ''
)

# 3. Auto-iniciar jota tras 4 segundos de pergamino
c = c.replace(
    "      document.getElementById('pant-pergamino').classList.add('show');",
    """      document.getElementById('pant-pergamino').classList.add('show');
      // Auto-iniciar jota tras 4 segundos
      setTimeout(iniciarJota, 4000);"""
)

# 4. Mejorar aleatoriedad - evitar las últimas 20
c = c.replace(
    """    // Aleatoriedad real — excluir la última jota escuchada
    const lastJota = sessionStorage.getItem('lastJota') || '';
    const disponibles = CFG.jotas.filter(j => j.a !== lastJota);
    const pool = disponibles.length > 0 ? disponibles : CFG.jotas;
    const seed = Date.now() ^ (performance.now() * 1000 | 0) ^ (Math.random() * 0xFFFFFFFF | 0);
    jota = pool[Math.abs(seed) % pool.length];
    sessionStorage.setItem('lastJota', jota.a);""",
    """    // Evitar las ultimas 20 jotas escuchadas
    let historial = JSON.parse(localStorage.getItem('cantabrana_hist') || '[]');
    const disponibles = CFG.jotas.filter(j => !historial.includes(j.a));
    const pool = disponibles.length > 0 ? disponibles : CFG.jotas;
    const seed = Date.now() ^ (performance.now() * 1000 | 0) ^ (Math.random() * 0xFFFFFFFF | 0);
    jota = pool[Math.abs(seed) % pool.length];
    historial.push(jota.a);
    if (historial.length > 20) historial = historial.slice(-20);
    try { localStorage.setItem('cantabrana_hist', JSON.stringify(historial)); } catch(e) {}"""
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')