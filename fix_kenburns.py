import re
c = open('index.html', 'r', encoding='utf-8').read()

# CSS Ken Burns
kenburns_css = """
@keyframes kenburns1{0%{transform:scale(1) translate(0,0)}100%{transform:scale(1.15) translate(-3%,-2%)}}
@keyframes kenburns2{0%{transform:scale(1) translate(0,0)}100%{transform:scale(1.12) translate(2%,-3%)}}
@keyframes kenburns3{0%{transform:scale(1.1) translate(-2%,0)}100%{transform:scale(1) translate(2%,2%)}}
@keyframes kenburns4{0%{transform:scale(1) translate(2%,2%)}100%{transform:scale(1.15) translate(-2%,-1%)}}
#kb-fondo{position:fixed;inset:0;z-index:5;overflow:hidden;display:none;background:#000;}
#kb-fondo.show{display:block;}
#kb-img{position:absolute;inset:-10%;width:120%;height:120%;object-fit:cover;opacity:0;transition:opacity 1.5s ease;}
#kb-img.show{opacity:1;}
"""
c = c.replace('/* VENTANAS INTRO */', kenburns_css + '\n/* VENTANAS INTRO */')

# HTML Ken Burns
kb_html = """<!-- KEN BURNS FONDO -->
<div id="kb-fondo">
  <img id="kb-img" src="" alt="">
</div>

"""
c = c.replace('<!-- VENTANAS INTRO -->', kb_html + '<!-- VENTANAS INTRO -->')

# JS Ken Burns - reemplazar mostrarFondoInicio
old_fondo = re.search(r'\(function mostrarFondoInicio\(\)\{.*?\}\)\(\);', c, re.DOTALL)
if old_fondo:
    nueva_fondo = """(function mostrarFondoInicio(){
    const IMGS = [
      'video/intro/rustico1.jpg','video/intro/rustico2.jpg',
      'video/intro/rustico3.jpg','video/intro/rustico4.jpg'
    ];
    const ANIMS = ['kenburns1','kenburns2','kenburns3','kenburns4'];
    const idx = Math.floor(Math.random()*IMGS.length);
    const div = document.getElementById('kb-fondo');
    const img = document.getElementById('kb-img');
    div.classList.add('show');
    img.src = IMGS[idx];
    img.onload = () => {
      img.classList.add('show');
      img.style.animation = ANIMS[idx] + ' 12s ease-in-out forwards';
    };
  })();"""
    c = c.replace(old_fondo.group(0), nueva_fondo)

# Ocultar kb-fondo al pulsar iniciar
c = c.replace(
    "  const divIntro=document.getElementById('video-intro');\n  divIntro.style.transition='opacity 0.8s ease';\n  divIntro.style.opacity='0';\n  setTimeout(()=>{divIntro.style.display='none';divIntro.style.opacity='1';divIntro.style.zIndex='9';},800);",
    """  const kbDiv=document.getElementById('kb-fondo');
  kbDiv.style.transition='opacity 0.8s ease';
  kbDiv.style.opacity='0';
  setTimeout(()=>{kbDiv.style.display='none';kbDiv.style.opacity='1';},800);"""
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')