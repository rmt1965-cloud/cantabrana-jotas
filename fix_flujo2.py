import re
c = open('index.html', 'r', encoding='utf-8').read()

# Nuevo CSS para fondo del splash
c = c.replace(
    '#loading{position:fixed;inset:0;z-index:100;background:#000;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:20px;transition:opacity 1.2s ease;}',
    '#loading{position:fixed;inset:0;z-index:100;background:rgba(0,0,0,.75);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:20px;transition:opacity 1.2s ease;-webkit-backdrop-filter:blur(4px);backdrop-filter:blur(4px);}'
)

# Mostrar video/foto de fondo inmediatamente al cargar
c = c.replace(
    "  keepScreen();\n  \n  // Detectar audio del QR",
    """  keepScreen();

  // Mostrar media de fondo inmediatamente
  (function mostrarFondoInicio(){
    const MEDIA = [
      {t:'v',s:'video/intro_web/video_02.mp4'},{t:'v',s:'video/intro_web/video_03.mp4'},
      {t:'v',s:'video/intro_web/video_04.mp4'},{t:'v',s:'video/intro_web/video_05.mp4'},
      {t:'v',s:'video/intro_web/video_06.mp4'},{t:'v',s:'video/intro_web/video_07.mp4'},
      {t:'v',s:'video/intro_web/video_12.mp4'},{t:'v',s:'video/intro_web/video_13.mp4'},
      {t:'v',s:'video/intro_web/video_14.mp4'},{t:'v',s:'video/intro_web/video_16.mp4'},
      {t:'v',s:'video/intro_web/video_17.mp4'},{t:'v',s:'video/intro_web/video_19.mp4'},
      {t:'i',s:'video/intro/rustico1.jpg'},{t:'i',s:'video/intro/rustico2.jpg'},
      {t:'i',s:'video/intro/rustico3.jpg'},{t:'i',s:'video/intro/rustico4.jpg'},
    ];
    const esMobil=/Mobi|Android|iPhone|iPad/i.test(navigator.userAgent);
    const pool=esMobil?MEDIA.filter(m=>m.t==='i'):MEDIA;
    const item=pool[Math.floor(Math.random()*pool.length)];
    const div=document.getElementById('video-intro');
    div.style.zIndex='5';
    div.classList.add('show');
    if(item.t==='v'){
      const vid=document.getElementById('vid');
      vid.src=item.s;vid.loop=true;
      vid.play().catch(()=>{});
    } else {
      const vid=document.getElementById('vid');
      vid.style.display='none';
      const img=document.createElement('img');
      img.src=item.s;
      img.style.cssText='position:absolute;inset:0;width:100%;height:100%;object-fit:cover;';
      div.appendChild(img);
    }
  })();

  // Detectar audio del QR"""
)

# Al pulsar iniciar - ocultar video fondo y continuar
c = c.replace(
    """  iniciarAmbiente();
  document.getElementById('loading').classList.add('fade');
  setTimeout(async()=>{
    await reproducirVideoIntro();
    await mostrarVentanas();""",
    """  iniciarAmbiente();
  document.getElementById('loading').classList.add('fade');
  // Ocultar video de fondo
  const divIntro=document.getElementById('video-intro');
  divIntro.style.transition='opacity 0.8s ease';
  divIntro.style.opacity='0';
  setTimeout(()=>{divIntro.style.display='none';divIntro.style.opacity='1';divIntro.style.zIndex='9';},800);
  setTimeout(async()=>{
    await mostrarVentanas();"""
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')