c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    '  // Cargar pergamino local\n  const pIdx',
    '  // Mostrar ventanas\n  await mostrarVentanas();\n\n  // Cargar pergamino local\n  const pIdx'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')