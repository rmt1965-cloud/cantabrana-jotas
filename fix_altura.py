c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace('.perg-outer{', '.perg-outer{\n  min-height:400px;')
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')