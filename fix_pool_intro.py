import os, json, re

# Solo fotos de extra y rusticas para el intro
fotos_intro = []
for f in sorted(os.listdir('fotos/extra')):
    if f.lower().endswith(('.jpg','.jpeg','.png')) and not f.startswith('.'):
        fotos_intro.append('fotos/extra/' + f)

# Añadir rusticas
for f in ['rustico1.jpg','rustico2.jpg','rustico3.jpg','rustico4.jpg']:
    fotos_intro.append('video/intro/' + f)

c = open('index.html', 'r', encoding='utf-8').read()
c = re.sub(
    r'const FOTOS_POOL = \[.*?\];',
    'const FOTOS_POOL = ' + json.dumps(fotos_intro) + ';',
    c, flags=re.DOTALL
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo -', len(fotos_intro), 'fotos en pool intro')
