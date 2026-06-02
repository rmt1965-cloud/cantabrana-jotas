c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'id="perg-img" src="" alt=""',
    'id="perg-img" src="fotos/pergaminos/pergamino01.jpg" alt="Pergamino"'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')