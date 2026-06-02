c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'font-size:clamp(8px,2vw,10px);',
    'font-size:clamp(11px,3vw,14px);'
)
c = c.replace(
    'margin-top:14px;',
    'margin-top:20px;'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')