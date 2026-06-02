c = open('index.html', 'r', encoding='utf-8').read()

# 1. Cantabrana más grande con aura
c = c.replace(
    'font-size:clamp(14px,4vw,20px);',
    'font-size:clamp(22px,7vw,36px);'
)
c = c.replace(
    '.ld-titulo{',
    '''.ld-titulo{
  text-shadow:0 0 40px rgba(200,146,42,.8), 0 0 80px rgba(200,146,42,.4);'''
)

# 2. Añadir slideshow de ventanas antes del pergamino
slideshow = """
#ventanas-slide{
  position:fixed;inset:0;z-index:8;
  background:#000;
  display:none;align-items:center;justify-content:center;
}
#ventanas-slide.show{display:flex}
#ventana-img{
  max-width:100%;max-height:100%;
  object-fit:contain;
  opacity:0;transition:opacity 1.5s ease;
}
#ventana-img.show{opacity:1}
"""
c = c.replace('/* PERGAMINO */', slideshow + '\n/* PERGAMINO */')

# 3. Añadir HTML del slideshow
c = c.replace(
    '<!-- LOADING -->',
    '''<!-- VENTANAS SLIDESHOW -->
<div id="ventanas-slide">
  <img id="ventana-img" src="" alt="Cantabrana">
</div>

<!-- LOADING -->'''
)

# 4. Añadir función slideshow antes de init
slideshow_js = """
const VENTANAS = ['fotos/ventanas/ventana1.jpg','fotos/ventanas/ventana3.jpg','fotos/ventanas/ventana4.png'];

async function mostrarVentanas(){
  return new Promise(resolve => {
    let idx = 0;
    const slide = document.getElementById('ventanas-slide');
    const img = document.getElementById('ventana-img');
    slide.classList.add('show');
    
    function siguiente(){
      if (idx >= VENTANAS.length) {
        slide.style.opacity = '0';
        slide.style.transition = 'opacity 1s ease';
        setTimeout(() => { slide.style.display='none'; resolve(); }, 1000);
        return;
      }
      img.classList.remove('show');
      setTimeout(() => {
        img.src = VENTANAS[idx++];
        img.onload = () => {
          img.classList.add('show');
          setTimeout(siguiente, 2500);
        };
        img.onerror = siguiente;
      }, 500);
    }
    siguiente();
  });
}
"""
c = c.replace('async function init(){', slideshow_js + '\nasync function init(){')

# 5. Llamar slideshow en init
c = c.replace(
    '  // Cargar pergamino local\n  const pIdx',
    '  // Mostrar ventanas primero\n  await mostrarVentanas();\n\n  // Cargar pergamino local\n  const pIdx'
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')