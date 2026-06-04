with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

old = '#v-img{position:absolute;inset:0;width:100%;height:100%;max-height:60vh;top:50%;transform:translateY(-50%);object-fit:cover;background:transparent;opacity:0;transition:opacity 1.5s ease;z-index:1;}'
new = '#v-img{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:90%;max-width:480px;max-height:72vh;object-fit:contain;background:transparent;opacity:0;transition:opacity 1.5s ease;z-index:1;}'

if old in c:
    c = c.replace(old, new)
    print('OK')
else:
    print('WARN no encontrado exacto:')
    import re
    m = re.search(r'#v-img\{[^}]+\}', c)
    if m:
        print('Encontrado:', m.group(0))

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')