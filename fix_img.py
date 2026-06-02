c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'width:100%;display:block;border-radius:4px;',
    'width:100%;min-height:300px;display:block;border-radius:4px;background:#2a1a08;'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')