import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

orig = c

# 1. Pergamino +2s (1200->3200)
c = c.replace('resolve();},1200)', 'resolve();},3200)')
print('1 pergamino +2s:', 'OK' if c!=orig else 'WARN')

# 2. Aleatoriedad real fotos intro
m = re.search(r'[ \t]*const fotos_intro=shuffle\(CFG\.fotos_intro\);', c)
if m:
    ind = re.match(r'([ \t]*)', m.group()).group(1)
    rep = (ind + 'let histI=[];try{histI=JSON.parse(localStorage.getItem("cant_intro")||"[]");}catch(e){}\n' +
           ind + 'let noVistasI=CFG.fotos_intro.filter(f=>!histI.includes(f));\n' +
           ind + 'if(noVistasI.length<3){histI=[];noVistasI=CFG.fotos_intro;}\n' +
           ind + 'const fotos_intro=shuffle(noVistasI);\n' +
           ind + 'const nvi=[...histI,...fotos_intro.slice(0,3)].slice(-Math.max(3,Math.floor(CFG.fotos_intro.length*0.6)));\n' +
           ind + 'try{localStorage.setItem("cant_intro",JSON.stringify(nvi));}catch(e){}')
    c = c[:m.start()] + rep + c[m.end():]
    print('2 aleatoriedad fotos intro: OK')

# 3. v-img ventanas: tamaño proporcionado
c = c.replace(
    '#v-img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;background:transparent;opacity:0;transition:opacity 1.5s ease;z-index:1;}',
    '#v-img{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:90%;max-width:500px;max-height:70vh;object-fit:contain;background:transparent;opacity:0;transition:opacity 1.5s ease;z-index:1;}'
)
print('3 v-img ventanas:', 'OK' if c!=orig else 'WARN')

# 4. Portada loading mas compacta
c = c.replace('font-size:clamp(28px,8vw,44px);letter-spacing:8px;', 'font-size:clamp(22px,6vw,36px);letter-spacing:6px;')
c = c.replace('font-size:clamp(18px,5.5vw,28px);color:rgba(240,192,96,.95);letter-spacing:3px;', 'font-size:clamp(15px,4.5vw,22px);color:rgba(240,192,96,.95);letter-spacing:3px;')
c = c.replace('flex-direction:column;gap:16px;', 'flex-direction:column;gap:10px;')
print('4 portada compacta: OK')

# 5. Preload + Ken Burns en carrusel
if "_preload=null" not in c:
    c = c.replace(
        'function mostrarFoto(idx){',
        'let _preload=null;\nfunction precargarFoto(idx){if(!fotos.length)return;_preload=new Image();_preload.src=fotos[(idx+1)%fotos.length];}\nfunction mostrarFoto(idx){'
    )
    print('5a preload: OK')

old_onload = "img.onload=()=>{setTimeout(()=>{trans.classList.remove('on');img.classList.add('show');},150);};"
new_onload = "img.onload=()=>{const kbs=['kenburns1','kenburns2','kenburns3','kenburns4'];img.style.animation=kbs[idx%4]+' '+(CFG.dur_foto+CFG.dur_trans+1)+'s ease-in-out forwards';setTimeout(()=>{trans.classList.remove('on');img.classList.add('show');},150);precargarFoto(idx);};"
c = c.replace(old_onload, new_onload)
c = c.replace("trans.classList.add('on');img.classList.remove('show');", "trans.classList.add('on');img.classList.remove('show');img.style.animation='none';")
print('5b Ken Burns: OK')

# 6. Fad