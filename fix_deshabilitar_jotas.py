with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

orig = c

# Eliminar jotas 36 y 37 del array CFG.jotas
# 36: CANTO IGLESIA LATÍN -- archivo con --36
# 37: SALVE -- archivo con --37
import re

# Eliminar líneas completas de jotas 36 y 37
c = re.sub(r"\s*\{a:'[^']*--36\.mp3',[^}]+\},?\n?", '\n', c)
c = re.sub(r"\s*\{a:'[^']*--37\.mp3',[^}]+\},?\n?", '\n', c)

cambios = orig.count('--36.mp3') + orig.count('--37.mp3') - c.count('--36.mp3') - c.count('--37.mp3')
print(f'Jotas eliminadas: {cambios}')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado OK')