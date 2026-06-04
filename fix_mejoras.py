import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
orig = c

# MEJORA 1+2: Preload + Ken Burns
if "_preload=null" not in c:
    c = c.replace(
        "function mostrarFoto(idx){",
        "let _preload=null;\nfunction precargarFoto(idx){if(!fotos.length)return;_preload=new Image();_preload.src=fotos[(idx+1)%fotos.length];}\nfunction mostrarFoto(idx){"
    )
    print("OK preload")

old_onload = "img.onload=()=>{setTimeout(()=>{trans.classList.remove('on');img.classList.add('show');},150);};"
new_onload = "img.onload=()=>{const kbs=['kenburns1','kenburns2','kenburns3','kenburns4'];img.style.animation=kbs[idx%4]+' '+(CFG.dur_foto+CFG.dur_trans+1)+'s ease-in-out forwards';setTimeout(()=>{trans.classList.remove('on');img.classList.add('show');},150);precargarFoto(idx);};"
if old_onload in c:
    c = c.replace(old_onload, new_onload)
    print("OK Ken Burns")
else:
    print("WARN Ken Burns no encontrado")

old_trans = "trans.classList.add('on');img.classList.remove('show');"
if old_trans in c:
    c = c.replace(old_trans, "trans.classList.add('on');img.classList.remove('show');img.style.animation='none';")
    print("OK reset animacion")

# MEJORA 3: Fade suave ambiente
old_fade = "let v=aAmb.volume;const fu=setInterval(()=>{v=Math.min(v+0.02,0.45);aAmb.volume=v;if(v>=0.45)clearInterval(fu);},100);"
new_fade = "let v=aAmb.volume;const fu=setInterval(()=>{v=Math.min(v+0.008,0.45);aAmb.volume=v;if(v>=0.45)clearInterval(fu);},60);"
if old_fade in c:
    c = c.replace(old_fade, new_fade)
    print("OK fade suave")
else:
    print("WARN fade no encontrado")

# MEJORA 4: Feedback tactil
old_btn = "cursor:pointer;border-radius:2px;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);}"
new_btn = "cursor:pointer;border-radius:2px;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);transition:transform .12s ease,background .12s ease;-webkit-tap-highlight-color:transparent;}\n.btn:active{transform:scale(0.96);background:rgba(200,146,42,.2);}"
if old_btn in c:
    c = c.replace(old_btn, new_btn)
    print("OK feedback tactil")
else:
    print("WARN feedback no encontrado")

# MEJORA 5: Link manifest
if 'manifest.json' not in c:
    c = c.replace(
        '<meta name="apple-mobile-web-app-capable" content="yes">',
        '<meta name="apple-mobile-web-app-capable" content="yes">\n<link rel="manifest" href="manifest.json">'
    )
    print("OK manifest link")

open('index.html', 'w', encoding='utf-8').write(c)
print("Guardado OK")