import re
c = open('index.html', 'r', encoding='utf-8').read()

# Añadir CSS para video final
css_final = """
#video-final{position:fixed;inset:0;z-index:45;background:#000;display:none;align-items:center;justify-content:center;}
#video-final.show{display:flex}
#vid-final{width:100%;height:100%;object-fit:cover;}
#video-final-fade{position:absolute;inset:0;background:#000;opacity:0;transition:opacity 1.5s ease;}
#video-final-fade.on{opacity:1}
"""
c = c.replace('#pant-final{', css_final + '\n#pant-final{')

# Añadir HTML para video final
html_final = """<!-- VIDEO FINAL -->
<div id="video-final">
  <video id="vid-final" src="" playsinline muted></video>
  <div id="video-final-fade"></div>
</div>

"""
c = c.replace('<!-- PANTALLA FINAL -->', html_final + '<!-- PANTALLA FINAL -->')

# Añadir JS función video final
js_final = """
function reproducirVideoFinal(callback) {
  const VIDEOS = [
    'video/final/video_08.mp4','video/final/video_09.mp4',
    'video/final/video10.mp4','video/final/video11.mp4','video/final/video99.mp4'
  ];
  const src = VIDEOS[Math.floor(Math.random() * VIDEOS.length)];
  const div  = document.getElementById('video-final');
  const vid  = document.getElementById('vid-final');
  const fade = document.getElementById('video-final-fade');
  div.classList.add('show');
  vid.src = src;
  vid.play().catch(() => callback());
  vid.onended = () => {
    fade.classList.add('on');
    setTimeout(() => { div.style.display='none'; callback(); }, 1500);
  };
  setTimeout(() => { div.style.display='none'; callback(); }, 20000);
}
"""
c = c.replace('function cargarSelloFinal()', js_final + '\nfunction cargarSelloFinal()')

# Llamar video final antes de mostrar pantalla final
c = c.replace(
    "    cargarSelloFinal();\n    document.getElementById('pant-repro').style.display='none';\n    document.getElementById('pant-final').classList.add('show');",
    """    document.getElementById('pant-repro').style.display='none';
    reproducirVideoFinal(() => {
      cargarSelloFinal();
      document.getElementById('pant-final').classList.add('show');
    });"""
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')