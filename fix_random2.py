c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    "    const seed = Date.now() ^ (Math.random() * 0xFFFFFFFF | 0);\n    jota = CFG.jotas[Math.abs(seed) % CFG.jotas.length];",
    """    // Aleatoriedad real — excluir la última jota escuchada
    const lastJota = sessionStorage.getItem('lastJota') || '';
    const disponibles = CFG.jotas.filter(j => j.a !== lastJota);
    const pool = disponibles.length > 0 ? disponibles : CFG.jotas;
    const seed = Date.now() ^ (performance.now() * 1000 | 0) ^ (Math.random() * 0xFFFFFFFF | 0);
    jota = pool[Math.abs(seed) % pool.length];
    sessionStorage.setItem('lastJota', jota.a);"""
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')