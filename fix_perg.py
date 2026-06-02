c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace('LOCAL', 'fotos/pergaminos/pergamino0' + str(__import__("random").randint(1,5)) + '.png')
# Añadir array local al CFG
c = c.replace("pergaminos_servidor: 'LOCAL'", "pergaminos_local: ['fotos/pergaminos/pergamino01.png','fotos/pergaminos/pergamino02.png','fotos/pergaminos/pergamino03.png','fotos/pergaminos/pergamino04.png','fotos/pergaminos/pergamino05.png']")
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')