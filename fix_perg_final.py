c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'font-size:clamp(18px,5.5vw,26px);font-weight:700;',
    'font-size:clamp(22px,7vw,34px);font-weight:800;'
)
c = c.replace(
    "font-size:clamp(8px,2vw,10px);",
    "font-size:clamp(14px,4vw,18px);font-weight:800;"
)
c = c.replace(
    "color:rgba(60,30,5,.5);",
    "color:rgba(10,5,5,.85);"
)
c = c.replace(
    "color:rgba(40,20,5,.88);",
    "color:rgba(10,5,5,.92);"
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')