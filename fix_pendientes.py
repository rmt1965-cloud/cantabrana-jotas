with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

orig = c

# v-img: corregir conflicto inset+top
c = c.replace(
    '#v-img{position:absolute;inset:0;width:100%;height:100%;max-height:60vh;top:50%;transform:translateY(-50%);object-fit:cover;background:transparent;opacity:0;transition:opacity 1.5s ease;z-index:1;}',
    '#v-img{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:90%;max-width:500px;max-height:70vh;object-fit:contain;background:transparent;opacity:0;transition:opacity 1.5s ease;z-index:1;}'
)
print('v-img:', 'OK' if c!=orig else 'WARN')

# fade ambiente final suave
c2 = c
c = c.replace(
    'let v=aAmb.volume;const fu=setInterval(()=>{v=Math.min(v+0.02,0.45);aAmb.volume=v;if(v>=0.45)clearInterval(fu);},100);',
    'let v=aAmb.volume;const fu=setInterval(()=>{v=Math.min(v+0.008,0.45);aAmb.volume=v;if(v>=0.45)clearInterval(fu);},60);'
)
print('fade ambiente:', 'OK' if c!=c2 else 'WARN')

# feedback tactil botones
c3 = c
c = c.replace(
    'cursor:pointer;border-radius:2px;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);}',
    'cursor:pointer;border-radius:2px;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);transition:transform .12s ease,background .12s ease;-webkit-tap-highlight-color:transparent;}\n.btn:active{transform:scale(0.96);background:rgba(200,146,42,.2);}'
)
print('feedback tactil:', 'OK' if c!=c3 else 'WARN')

# manifest link
c4 = c
if 'manifest.json' not in c:
    c = c.replace(
        '<meta name="apple-mobile-web-app-capable" content="yes">',
        '<meta name="apple-mobile-web-app-capable" content="yes">\n<link rel="manifest" href="manifest.json">'
    )
print('manifest:', 'OK' if c!=c4 else 'ya existia')

# pergamino fade out suave
c5 = c
c = c.replace(
    "document.getElementById('pant-perg').style.opacity='0';",
    "const perg=document.getElementById('pant-perg');perg.style.transition='opacity 2s ease';perg.style.opacity='0';"
)
print('pergamino fade:', 'OK' if c!=c5 else 'WARN')

# reproductor fade in
c6 = c
c = c.replace(
    "document.getElementById('pant-repro').classList.add('show');",
    "const pr=document.getElementById('pant-repro');pr.style.opacity='0';pr.classList.add('show');pr.style.transition='opacity 1.5s ease';setTimeout(()=>{pr.style.opacity='1';},50);"
)
print('repro fade in:', 'OK' if c!=c6 else 'WARN')

# ui-bot oculto en fin
c7 = c
c = c.replace(
    "function finJota(){\n  if(jotaFin)return;jotaFin=true;",
    "function finJota(){\n  if(jotaFin)return;jotaFin=true;\n  const ub=document.getElementById('ui-bot');ub.style.opacity='0';ub.style.pointerEvents='none';"
)
print('ui-bot fin:', 'OK' if c!=c7 else 'WARN')

open('index.html', 'w', encoding='utf-8').write(c)
print('\nGuardado OK')