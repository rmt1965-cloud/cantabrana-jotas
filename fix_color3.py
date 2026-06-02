c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    "document.querySelector('.aviso').style.color = 'rgba(245,235,220,.95)';",
    "document.querySelector('.aviso').style.color = 'rgba(10,5,5,.95)';"
)
c = c.replace(
    "document.querySelector('.toca').style.color = 'rgba(220,200,160,.8)';",
    "document.querySelector('.toca').style.color = 'rgba(10,5,5,.8)';"
)
c = c.replace(
    "line-height:1.65;",
    "line-height:1.8;word-break:break-word;"
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')