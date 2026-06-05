with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    '#d-img{position:absolute;inset:-10%;width:120%;height:120%;object-fit:cover;opacity:0.65;}',
    '#d-img{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:88%;max-width:500px;max-height:75vh;object-fit:contain;opacity:0.9;}'
)
print('OK d-img ajustado' if 'max-width:500px' in c else 'WARN')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')