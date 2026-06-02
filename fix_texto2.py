c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'font-size:clamp(16px,5vw,24px);',
    'font-size:clamp(18px,6vw,28px);'
)
c = c.replace(
    'width:75%;',
    'width:82%;'
)
c = c.replace(
    'line-height:1.8;word-break:break-word;',
    'line-height:2.0;word-break:break-word;'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')