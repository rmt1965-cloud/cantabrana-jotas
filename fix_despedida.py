import re
c = open('index.html', 'r', encoding='utf-8').read()

# CSS pantalla despedida
css_desp = """
#pant-despedida{position:fixed;inset:0;z-index:42;background:#000;display:none;align-items:center;justify-content:center;flex-direction:column;}
#pant-despedida.show{display:flex}
#desp-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0.6;}
#desp-texto{position:absolute;bottom:15%;left:50%;transform:translateX(-50%);width:85%;text-align:center;font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(18px,5.5vw,28px);font-weight:600;color:rgba(245,230,190,.95);text-shadow:0 2px 20px rgba(0,0,0,.95),0 0 40px rgba(200,146,42,.3);line-height:1.7;}
"""
c = c.replace('#pant-final{', css_desp + '\n#pant-final{')

# HTML pantalla despedida
html_desp = """<!-- DESPEDIDA -->
<div id="pant-despedida">
  <img id="desp-img" src="" alt="">
  <div id="desp-texto"></div>
</div>

"""
c = c.replace('<!-- PANTALLA FINAL -->', html_desp + '<!-- PANTALLA FINAL -->')

# JS despedida
js_desp = """
function mostrarDespedida(callback) {
  const VISTAS = [
    'fotos/vistas/A01.jpg','fotos/vistas/A02.png','fotos/vistas/A03.jpg',
    'fotos/vistas/A04.jpg','fotos/vistas/A05.jpg','fotos/vistas/A06.jpg',
    'fotos/vistas/A07.jpg','fotos/vistas/A08.jpg','fotos/vistas/A09.png',
    'fotos/vistas/A10.jpg'
  ];
  const TEXTOS = [
    'Cantabrana siempre estará aquí. Vuelve cuando quieras.',
    'Gracias por escuchar. Gracias por recordar.',
    'Esta música seguirá sonando. Como siempre ha sonado.',
    'Lo que acabas de escuchar no se olvida fácilmente.',
    'Cantabrana, donde el tiempo respira despacio.',
    'Gracias por ser parte de esta memoria.',
    'La tradición vive porque hay quien la escucha.'
  ];
  const idxV = crypto.getRandomValues(new Uint32Array(1))[0] % VISTAS.length;
  const idxT = crypto.getRandomValues(new Uint32Array(1))[0] % TEXTOS.length;
  const div = document.getElementById('pant-despedida');
  const img = document.getElementById('desp-img');
  const txt = document.getElementById('desp-texto');
  img.src = VISTAS[idxV];
  txt.textContent = TEXTOS[idxT];
  div.classList.add('show');
  setTimeout(() => {
    div.style.transition = 'opacity 1.5s ease';
    div.style.opacity = '0';
    setTimeout(() => { div.style.display='none'; callback(); }, 1500);
  }, 5000);
}
"""
c = c.replace('function cargarSelloFinal()', js_desp + '\nfunction cargarSelloFinal()')

# Llamar despedida antes de pantalla final
c = c.replace(
    "    document.getElementById('pant-repro').style.display='none';\n    document.getElementById('pant-final').classList.add('show');",
    """    document.getElementById('pant-repro').style.display='none';
    mostrarDespedida(() => {
      cargarSelloFinal();
      document.getElementById('pant-final').classList.add('show');
    });"""
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')