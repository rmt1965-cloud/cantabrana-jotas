import re
c = open('index.html', 'r', encoding='utf-8').read()

# Encontrar y eliminar la primera funcion mostrarDespedida duplicada
partes = c.split('function mostrarDespedida(callback) {')
if len(partes) >= 3:
    # Eliminar la primera ocurrencia
    primera_fin = partes[1].find('\n}')
    partes[1] = partes[1][primera_fin+2:]
    c = 'function mostrarDespedida(callback) {'.join(partes)
    print('Duplicado eliminado')
else:
    print('No hay duplicado')

open('index.html', 'w', encoding='utf-8').write(c)