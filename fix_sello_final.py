c = open('index.html', 'r', encoding='utf-8').read()

# Añadir imagen sello aleatorio después del texto final
c = c.replace(
    '<div class="fin-btns">',
    '''<img id="sello-final" src="" alt="Sello" style="width:clamp(80px,20vw,130px);margin-top:16px;filter:drop-shadow(0 4px 16px rgba(140,20,20,.7));animation:sello-glow 3s ease-in-out infinite;">
  <div class="fin-btns">'''
)

# JS para cargar sello aleatorio en pantalla final
c = c.replace(
    'function finJota() {',
    '''function cargarSelloFinal() {
  const sellos = ['fotos/sellos/sello1.jpg','fotos/sellos/sello4.jpg','fotos/sellos/sello5.jpg'];
  const idx = Math.floor(Math.random() * sellos.length);
  document.getElementById('sello-final').src = sellos[idx];
}

function finJota() {'''
)

# Llamar cargarSelloFinal al mostrar pantalla final
c = c.replace(
    "    document.getElementById('pant-final').classList.add('show');",
    "    cargarSelloFinal();\n    document.getElementById('pant-final').classList.add('show');"
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')