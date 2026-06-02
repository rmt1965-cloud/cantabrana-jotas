c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'mix-blend-mode:multiply;',
    'mix-blend-mode:screen;'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')