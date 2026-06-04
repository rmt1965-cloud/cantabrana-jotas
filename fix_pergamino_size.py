with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Mas grande pero dentro de pantalla
c = c.replace(
    '.p-outer{position:relative;width:min(88vw,400px);',
    '.p-outer{position:relative;width:min(92vw,520px);'
)
c = c.replace(
    '#p-img{width:100%;min-height:350px;display:block;border-radius:4px;background:#2a1a08;object-fit:cover;}',
    '#p-img{width:100%;min-height:auto;max-height:82vh;display:block;border-radius:4px;background:#2a1a08;object-fit:contain;}'
)
print('OK' if '520px' in c else 'WARN')
open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')