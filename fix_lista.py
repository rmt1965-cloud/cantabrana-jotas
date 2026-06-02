import os, json, re

fotos = ['fotos/arcos/' + f for f in sorted(os.listdir('fotos/arcos')) 
         if f.lower().endswith(('.jpg','.jpeg','.png')) and f != '.gitkeep']

c = open('index.html', 'r', encoding='utf-8').read()
c = re.sub(
    r'const todas = \[.*?\];',
    'const todas = ' + json.dumps(fotos) + ';',
    c, flags=re.DOTALL
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo -', len(fotos), 'fotos')