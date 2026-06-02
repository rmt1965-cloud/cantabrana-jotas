c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    "img.onload = () => {",
    "img.onerror = () => { setTimeout(() => mostrarFoto(idx + 1), 300); };\n    img.onload = () => {"
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')