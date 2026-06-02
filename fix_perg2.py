c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'font-size:clamp(14px,4vw,18px);font-weight:800;',
    'font-size:clamp(11px,3vw,14px);font-weight:600;'
)
c = c.replace(
    'font-size:clamp(22px,7vw,34px);font-weight:800;',
    'font-size:clamp(24px,8vw,38px);font-weight:800;'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')