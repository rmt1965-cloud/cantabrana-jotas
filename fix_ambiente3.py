c = open('index.html', 'r', encoding='utf-8').read()
# Quitar iniciarAmbiente del init - solo debe llamarse tras interaccion
lineas = c.split('\n')
nueva = []
skip = False
for l in lineas:
    if '// Iniciar m' in l and 'ambiente' in l.lower():
        skip = True
    elif skip and 'iniciarAmbiente()' in l:
        skip = False
        continue
    else:
        skip = False
    if not (skip and 'iniciarAmbiente' in l):
        nueva.append(l)
c = '\n'.join(nueva)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')