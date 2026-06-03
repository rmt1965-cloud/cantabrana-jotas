import re
c = open('index.html', 'r', encoding='utf-8').read()

# Reemplazar todo el bloque de ventanas
old = re.search(
    r'// 3 ventanas aleatorias del pool.*?CFG\.ventanas = todasVentanas\.slice\(0,3\);',
    c, re.DOTALL
)
if old:
    nuevo = """// 3 fotos aleatorias con frases del grupo en orden estricto
  CFG.ventanas = [
    { src: fotosAleatorias[0], leyenda: frasesAleatorias[0] },
    { src: fotosAleatorias[1], leyenda: frasesAleatorias[1] },
    { src: fotosAleatorias[2], leyenda: frasesAleatorias[2] },
  ];"""
    c = c.replace(old.group(0), nuevo)
    print('Reemplazado OK')
else:
    print('No encontrado')

open('index.html', 'w', encoding='utf-8').write(c)