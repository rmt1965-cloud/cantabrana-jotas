with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    '#f-img{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);max-width:90%;max-height:80vh;width:auto;height:auto;object-fit:contain;opacity:0;transition:opacity 1s ease;}',
    '#f-img{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);max-width:75%;max-height:65vh;width:auto;height:auto;object-fit:contain;opacity:0;transition:opacity 1s ease;}'
)
print('OK' if 'max-width:75%' in c else 'WARN')
open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')