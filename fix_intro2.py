import re
c = open('index.html', 'r', encoding='utf-8').read()

nueva = """async function reproducirVideoIntro() {
  return new Promise(resolve => {
    const MEDIA = [
      {t:'v',s:'video/intro/video_02.mp4'},{t:'v',s:'video/intro/video_03.mp4'},
      {t:'v',s:'video/intro/video_04.mp4'},{t:'v',s:'video/intro/video_05.mp4'},
      {t:'v',s:'video/intro/video_06.mp4'},{t:'v',s:'video/intro/video_07.mp4'},
      {t:'v',s:'video/intro/video_12.mp4'},{t:'v',s:'video/intro/video_13.mp4'},
      {t:'v',s:'video/intro/video_14.mp4'},{t:'v',s:'video/intro/video_16.mp4'},
      {t:'v',s:'video/intro/video_17.mp4'},{t:'v',s:'video/intro/video_19.mp4'},
      {t:'i',s:'video/intro/rustico1.jpg'},{t:'i',s:'video/intro/rustico2.jpg'},
      {t:'i',s:'video/intro/rustico3.jpg'},{t:'i',s:'video/intro/rustico4.jpg'},
    ];
    const item=MEDIA[Math.floor(Math.random()*MEDIA.length)];
    const div=document.getElementById('video-intro');
    const fade=document.getElementById('video-fade');
    div.classList.add('show');
    const fin=()=>{fade.classList.add('on');setTimeout(()=>{div.style.display='none';fade.classList.remove('on');resolve();},1500);};
    if(item.t==='v'){
      const vid=document.getElementById('vid');
      vid.style.display='';vid.src=item.s;
      vid.play().catch(()=>fin());
      vid.onended=fin;
      setTimeout(fin,15000);
    } else {
      const vid=document.getElementById('vid');
      vid.style.display='none';
      const img=document.createElement('img');
      img.src=item.s;
      img.style.cssText='position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity 1s ease;';
      div.appendChild(img);
      setTimeout(()=>{img.style.opacity='1';},100);
      setTimeout(()=>{fin();setTimeout(()=>{img.remove();vid.style.display='';},1600);},3500);
    }
  });
}"""

c = re.sub(r'async function reproducirVideoIntro\(\) \{.*?\n\}', nueva, c, flags=re.DOTALL)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')