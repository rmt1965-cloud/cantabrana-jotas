with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    '#d-img{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:88%;max-width:500px;max-height:75vh;object-fit:contain;opacity:0.9;}',
    '#d-img{width:88%;max-width:500px;max-height:75vh;object-fit:contain;opacity:0.9;position:relative;}'
)
print('OK d-img sin conflicto' if 'position:relative' in c else 'WARN')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')