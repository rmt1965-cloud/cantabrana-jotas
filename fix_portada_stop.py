with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

old = "function finJota(){\n  if(jotaFin)return;jotaFin=true;"
new = "function finJota(){\n  if(jotaFin)return;jotaFin=true;\n  clearTimeout(fotoTimer);fotoIdx=0;"

if old in c:
    c = c.replace(old, new)
    print('OK carrusel parado en finJota')
else:
    print('WARN no encontrado')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')