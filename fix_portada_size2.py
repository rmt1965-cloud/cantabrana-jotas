with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    "fi.style.maxWidth='75%';fi.style.maxHeight='65vh';",
    "fi.style.maxWidth='88%';fi.style.maxHeight='78vh';"
)
print('OK' if '88%' in c else 'WARN')
open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')