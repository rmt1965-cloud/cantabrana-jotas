with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

old = """  vistas: [
    'fotos/vistas/A01.jpg','fotos/vistas/A02.png','fotos/vistas/A03.jpg',
    'fotos/vistas/A04.jpg','fotos/vistas/A05.jpg','fotos/vistas/A06.jpg',
    'fotos/vistas/A07.jpg','fotos/vistas/A08.jpg','fotos/vistas/A09.png','fotos/vistas/A10.jpg',
  ],"""

new = """  vistas: [
    'fotos/vistas/A01.jpg','fotos/vistas/A02.JPG','fotos/vistas/A03.jpg',
    'fotos/vistas/A04.jpg','fotos/vistas/A05.jpg','fotos/vistas/A06.jpg',
    'fotos/vistas/A07.jpg','fotos/vistas/A08.jpg','fotos/vistas/A10.jpg',
  ],"""

if old in c:
    c = c.replace(old, new)
    print('OK vistas actualizadas')
else:
    print('WARN no encontrado exacto, buscando variante...')
    import re
    m = re.search(r"vistas:\s*\[.*?\],", c, re.DOTALL)
    if m:
        c = c[:m.start()] + new.strip() + c[m.end():]
        print('OK vistas variante')
    else:
        print('ERR no encontrado')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')