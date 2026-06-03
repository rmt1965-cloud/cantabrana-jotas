c = open('index.html', 'r', encoding='utf-8').read()

# Reemplazar función reproducirVideoIntro con versión que soporta imágenes y vídeos
nueva_funcion = """
async function reproducirVideoIntro() {
  return new Promise(resolve => {
    const MEDIA = [
      {tipo:'video', src:'video/intro/video_02.mp4'},
      {tipo:'video', src:'video/intro/video_03.mp4'},
      {tipo:'video', src:'video/intro/video_04.mp4'},
      {tipo:'video', src:'video/intro/video_05.mp4'},
      {tipo:'video', src:'video/intro/video_06.mp4'},
      {tipo:'video', src:'video/intro/video_07.mp4'},
      {tipo:'video', src:'video/intro/video_12.mp4'},
      {tipo:'video', src:'video/intro/video_13.mp4'},
      {tipo:'video', src:'video/intro/video_14.mp4'},
      {tipo:'video', src:'video/intro/video_16.mp4'},
      {tipo:'video', src:'video/intro/video_17.mp4'},
      {tipo:'video', src:'video/intro/video_19.mp4'},
      {tipo:'imagen', src:'video/intro/rustico1.jpg'},
      {tipo:'imagen', src:'video/intro/rustico2.jpg'},
      {tipo:'imagen', src:'video/intro/rustico3.jpg'},
      {tipo:'imagen', src:'video/intro/rustico4.jpg'},
    ];
    const item = MEDIA[Math.floor(Math.random() * MEDIA.length)];
    const div  = document.getElementById('video-intro');
    const fade = document.getElementById('video-fade');
    div.classList.add('show');

    if (item.tipo === 'video') {
      const vid = document.getElementById('vid');
      vid.src = item.src;
      vid.play().catch(() => resolve());
      vid.onended = () => {
        fade.classList.add('on');
        setTimeout(() => { div.style.display='none'; fade.classList.remove('on'); resolve(); }, 1500);
      };
      setTimeout(() => { div.style.display='none'; resolve(); }, 15000);
    } else {
      // Es imagen — mostrar 3 segundos
      const vid = document.getElementById('vid');
      vid.style.display = 'none';
      const img = document.createElement('img');
      img.src = item.src;
      img.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity 1s ease;';
      div.appendChild(img);
      setTimeout(() => { img.style.opacity = '1'; }, 100);
      setTimeout(() => {
        fade.classList.add('on');
        setTimeout(() => {
          div.style.display='none';
          fade.classList.remove('on');
          vid.style.display='';
          img.remove();
          resolve();
        }, 1500);
      }, 3000);
    }
  });
}
"""

# Reemplazar función antigua
import re
c = re.sub(r'async function reproducirVideoIntro\(\)\{.*?\}\n', nueva_funcion, c, flags=re.DOTALL)

# Activar llamada al video en init
c = c.replace(
    '    await mostrarVentanas();',
    '    await reproducir