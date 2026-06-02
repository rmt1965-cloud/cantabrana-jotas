c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'color:rgba(40,20,5,.88);',
    'color:rgba(120,10,10,.92);'
)
c = c.replace(
    'color:rgba(60,30,5,.5);',
    'color:rgba(100,5,5,.75);'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')