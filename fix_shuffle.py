c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'fotos = todas.sort(() => Math.random() - 0.5).slice(0, 20);',
    '''// Fisher-Yates shuffle para mejor aleatoriedad
  for (let i = todas.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [todas[i], todas[j]] = [todas[j], todas[i]];
  }
  fotos = todas;'''
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')