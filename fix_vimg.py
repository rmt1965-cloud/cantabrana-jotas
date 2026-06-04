with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

orig = c

# v-img: contain -> cover para que rellene proporcionado
c = c.replace(
    'object-fit:contain;background:transparent;',
    'object-fit:cover;background:transparent;'
)

print('OK' if c != orig else 'NO ENCONTRADO')
open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')