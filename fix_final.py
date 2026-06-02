import os, json, re

# Generar lista real de fotos desde la carpeta original
carpeta = r'C:\Users\Rafa\Desktop\V22\cantabrana-V22\media\fotos\arcos_puertas'
fotos = []
for f in sorted(os.listdir(carpeta)):
    if f.lower().endswith(('.jpg','.jpeg','.png')) and not f.startswith('.'):
        fotos.append('fotos/arcos/' + f)

c = open('index.html', 'r', encoding='utf-8').read()

# Fix fotos con lista real
c = re.sub(
    r'const lista = \[.*?\];',
    'const lista = ' + json.dumps(fotos) + ';',
    c, flags=re.DOTALL
)

# Fix pergamino
c = c.replace(
    "const pUrl = CFG.pergaminos_local[Math.floor(Math.random()*5)];",
    "const pUrl = ['fotos/pergaminos/pergamino01.png','fotos/pergaminos/pergamino02.png','fotos/pergaminos/pergamino03.png','fotos/pergaminos/pergamino04.png','fotos/pergaminos/pergamino05.png'][Math.floor(Math.random()*5)];"
)

# Fix mostrarFallback
c = c.replace(
    "onerror=\"this.style.display='none';mostrarFallback()\"",
    "onerror=\"this.style.display='none'\""
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo -', len(fotos), 'fotos')