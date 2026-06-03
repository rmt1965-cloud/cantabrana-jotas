c = open('index.html', 'r', encoding='utf-8').read()

# Añadir fondo difuminado a las ventanas
c = c.replace(
    '#vimg{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;background:#000;opacity:0;transition:opacity 1.5s ease;}',
    '#vimg{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;background:#000;opacity:0;transition:opacity 1.5s ease;z-index:1;}'
)

# Añadir CSS para blur de fondo
c = c.replace(
    '#ventanas-intro{position:fixed;inset:0;z-index:8;background:#000;display:none;align-items:center;justify-content:center;}',
    '#ventanas-intro{position:fixed;inset:0;z-index:8;background:#000;display:none;align-items:center;justify-content:center;overflow:hidden;}\n#vimg-blur{position:absolute;inset:-20px;width:calc(100% + 40px);height:calc(100% + 40px);object-fit:cover;filter:blur(20px) brightness(.4) saturate(.6);opacity:0;transition:opacity 1.5s ease;z-index:0;}'
)

# Añadir img blur en HTML
c = c.replace(
    '<img id="vimg" src="" alt="">',
    '<img id="vimg-blur" src="" alt="">\n  <img id="vimg" src="" alt="">'
)

# Actualizar JS para cargar blur
c = c.replace(
    "        img.src = data.src;",
    "        img.src = data.src;\n        document.getElementById('vimg-blur').src = data.src;\n        document.getElementById('vimg-blur').style.opacity = '1';"
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')