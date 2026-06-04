with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

orig = c

# v-img: limitar tamaño para que no ocupe toda la pantalla
c = c.replace(
    '#v-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;background:transparent;opacity:0',
    '#v-img{position:absolute;inset:0;width:100%;height:100%;max-height:60vh;top:50%;transform:translateY(-50%);object-fit:cover;background:transparent;opacity:0'
)

print('OK' if c != orig else 'NO ENCONTRADO')
open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')