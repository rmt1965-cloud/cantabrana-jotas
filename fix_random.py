c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'if (!jota) jota = CFG.jotas[Math.floor(Math.random() * CFG.jotas.length)];',
    """// Mejor aleatoriedad usando timestamp + crypto
  const seed = Date.now() ^ (Math.random() * 0xFFFFFFFF | 0);
  const idx = Math.abs(seed) % CFG.jotas.length;
  if (!jota) jota = CFG.jotas[idx];"""
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')