c = open('index.html', 'r', encoding='utf-8').read()

# Añadir botón de audio visible en el splash
c = c.replace(
    '<div id="ld-btn" onclick="arrancar()" ontouchstart="arrancar()">Pulsar para iniciar</div>',
    '<div id="ld-btn" onclick="arrancar()" ontouchstart="arrancar()">&#9654; Pulsar para iniciar con sonido</div>'
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')