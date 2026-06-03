c = open('index.html', 'r', encoding='utf-8').read()
# Quitar llamada al video
c = c.replace(
    '    await reproducirVideoIntro();\n',
    ''
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')