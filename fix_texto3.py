c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'Estas canciones son de otra época,<br>algunas pueden herir su sensibilidad',
    'Estas canciones<br>son de otra época,<br>algunas pueden herir<br>su sensibilidad'
)
c = c.replace(
    'font-style:italic;',
    'font-style:italic;font-weight:700;'
)
c = c.replace(
    "font-size:clamp(11px,3vw,14px);",
    "font-size:clamp(13px,3.5vw,16px);font-weight:800;color:rgba(10,5,5,.99)!important;"
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')