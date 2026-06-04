with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

orig = c

# f-img: contain centrado para ver fotos completas sin recorte
c = c.replace(
    '#f-img{max-width:100%;max-height:100%;object-fit:contain;opacity:0;transition:opacity 1s ease;}',
    '#f-img{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);max-width:100%;max-height:100%;width:auto;height:auto;object-fit:contain;opacity:0;transition:opacity 1s ease;}'
)
print('f-img centrado:', 'OK' if c!=orig else 'WARN')

# f-main necesita position relative para que f-img absolute funcione
c = c.replace(
    '#f-main{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;}',
    '#f-main{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;overflow:hidden;}'
)
print('f-main overflow:', 'OK')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado OK')