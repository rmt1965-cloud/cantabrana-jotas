c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'font-size:clamp(12px,3.5vw,17px);',
    'font-size:clamp(16px,5vw,24px);'
)
c = c.replace(
    'width:68%;',
    'width:75%;'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')