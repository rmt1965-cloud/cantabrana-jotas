c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    '  dur_foto: 4,',
    '  dur_foto: 3,'
)
c = c.replace(
    '  dur_trans: 1.0,',
    '  dur_trans: 0.5,'
)
# Quitar el delay de 600ms antes de empezar fotos
c = c.replace(
    'setTimeout(() => {\n    mostrarFoto(0);\n    aJota.play',
    'mostrarFoto(0);\n  setTimeout(() => {\n    aJota.play'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')