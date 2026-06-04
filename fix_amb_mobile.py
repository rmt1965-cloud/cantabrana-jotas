c = open('index.html', 'r', encoding='utf-8').read()

# Iniciar ambiente directamente en arrancar()
c = c.replace(
    'function arrancar(){\n  if(window._arrancado) return;\n  window._arrancado = true;',
    'function arrancar(){\n  if(window._arrancado) return;\n  window._arrancado = true;\n  iniciarAmbiente();'
)

# Quitar iniciarAmbiente del flujo principal
c = c.replace(
    '  // Iniciar ambiente\n  iniciarAmbiente();\n\n  // Ocultar loading',
    '  // Ocultar loading'
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')