c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    "  pergaminos_servidor: 'https://cantabrana-v22.onrender.com/api/media/random-pergamino',",
    "  pergaminos_local: ['fotos/pergaminos/pergamino01.png','fotos/pergaminos/pergamino02.png','fotos/pergaminos/pergamino03.png','fotos/pergaminos/pergamino04.png','fotos/pergaminos/pergamino05.png'],"
)
c = c.replace(
    "    const resp = await fetch(CFG.pergaminos_servidor);\n    if (resp.ok) {\n      const data = await resp.json();\n      if (data?.url) document.getElementById('perg-img').src = data.url;\n    }",
    "    const pUrl = CFG.pergaminos_local[Math.floor(Math.random()*5)];\n    document.getElementById('perg-img').src = pUrl;"
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')