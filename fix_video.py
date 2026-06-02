c = open('index.html', 'r', encoding='utf-8').read()

# CSS para el video
video_css = """
#video-intro{position:fixed;inset:0;z-index:9;background:#000;display:none;align-items:center;justify-content:center;}
#video-intro.show{display:flex}
#video-intro video{width:100%;height:100%;object-fit:cover;}
#video-fade{position:absolute;inset:0;background:#000;opacity:0;transition:opacity 1.5s ease;pointer-events:none;}
#video-fade.on{opacity:1}
"""
c = c.replace('/* VENTANAS INTRO */', video_css + '\n/* VENTANAS INTRO */')

# HTML para el video
video_html = """<!-- VIDEO INTRO -->
<div id="video-intro">
  <video id="vid" src="video/inicio.mp4" playsinline muted></video>
  <div id="video-fade"></div>
</div>

"""
c = c.replace('<!-- VENTANAS INTRO -->', video_html + '<!-- VENTANAS INTRO -->')

# JS para reproducir video antes de ventanas
video_js = """
async function reproducirVideoIntro() {
  return new Promise(resolve => {
    const div = document.getElementById('video-intro');
    const vid = document.getElementById('vid');
    const fade = document.getElementById('video-fade');
    div.classList.add('show');
    vid.play().catch(() => resolve());
    vid.onended = () => {
      fade.classList.add('on');
      setTimeout(() => { div.style.display = 'none'; resolve(); }, 1600);
    };
    // Timeout por si el video falla
    setTimeout(() => { div.style.display = 'none'; resolve(); }, 15000);
  });
}
"""
c = c.replace('async function mostrarVentanas()', video_js + '\nasync function mostrarVentanas()')

# Llamar video antes de ventanas
c = c.replace(
    '      await mostrarVentanas();',
    '      await reproducirVideoIntro();\n      await mostrarVentanas();'
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')