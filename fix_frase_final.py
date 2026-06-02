c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'La tradici&oacute;n vive en cada nota,<br>en cada puerta, en cada arco de piedra...<br><br>Gracias por escuchar.',
    'La tradici&oacute;n vive en cada nota,<br>en cada puerta,<br>en cada arco de piedra.<br><br>Gracias por escuchar.'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')