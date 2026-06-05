with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# v-img ventanas inicio: mas pequena para movil
c = c.replace(
    '#v-img{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:90%;max-width:480px;max-height:72vh;object-fit:contain;background:transparent;opacity:0;transition:opacity 1.5s ease;z-index:1;}',
    '#v-img{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:85%;max-width:360px;max-height:60vh;object-fit:contain;background:transparent;opacity:0;transition:opacity 1.5s ease;z-index:1;}'
)
print('OK v-img ajustado')

# f-img carrusel final: limitar tamaño
c = c.replace(
    '#f-img{max-width:100%;max-height:100%;object-fit:contain;opacity:0;transition:opacity 1s ease;}',
    '#f-img{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);max-width:88%;max-height:72vh;object-fit:contain;opacity:0;transition:opacity 1s ease;}'
)
print('OK f-img ajustado')

# dur_foto: 3s -> 5s (mas tiempo por foto)
c = c.replace('dur_foto: 3,', 'dur_foto: 5,')
print('OK dur_foto 3->5s')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')