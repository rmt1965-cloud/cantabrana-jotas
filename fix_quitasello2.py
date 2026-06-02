import re
c = open('index.html', 'r', encoding='utf-8').read()
# Eliminar todas las líneas con sello-final img
c = re.sub(r'  <img id="sello-final"[^>]+>\n?', '', c)
# Eliminar función cargarSelloFinal
c = re.sub(r'function cargarSelloFinal\(\)\{[^}]+\}\n?', '', c)
# Eliminar llamada a cargarSelloFinal
c = c.replace('cargarSelloFinal();', '')
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')