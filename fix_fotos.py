c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    "  fotos_servidor: 'https://cantabrana-v22.onrender.com/api/media/random-foto?categoria=fotos/arcos_puertas',",
    "  fotos_servidor: null,"
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')