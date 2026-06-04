with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

orig = c

# 1. Portada loading: boton mas pequeno y menos padding para que quepa todo
c = c.replace(
    'font-size:clamp(13px,4vw,17px);letter-spacing:4px;color:var(--gold);text-transform:uppercase;padding:16px 44px;border:2px solid rgba(200,146,42,.7);border-radius:4px;cursor:pointer;background:rgba(200,146,42,.12);min-width:200px;text-align:center;opacity:0;transition:opacity 1s ease;animation:pulse 1.8s ease-in-out infinite;margin-top:8px;}',
    'font-size:clamp(11px,3.5vw,14px);letter-spacing:3px;color:var(--gold);text-transform:uppercase;padding:11px 32px;border:2px solid rgba(200,146,42,.7);border-radius:4px;cursor:pointer;background:rgba(200,146,42,.12);min-width:160px;text-align:center;opacity:0;transition:opacity 1s ease;animation:pulse 1.8s ease-in-out infinite;margin-top:4px;}'
)
print('1 boton portada:', 'OK' if c!=orig else 'WARN')

# 2. f-img: limitar tamaño maximo para que no ocupe toda la pantalla
c2 = c
c = c.replace(
    '#f-img{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);max-width:100%;max-height:100%;width:auto;height:auto;object-fit:contain;opacity:0;transition:opacity 1s ease;}',
    '#f-img{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);max-width:90%;max-height:80vh;width:auto;height:auto;object-fit:contain;opacity:0;transition:opacity 1s ease;}'
)
print('2 f-img tamanio:', 'OK' if c!=c2 else 'WARN')

# 3. Pantalla final: reducir tamaños para que quepa todo
c = c.replace(
    '.fin-tit{font-family:\'Cinzel\',serif;font-size:clamp(30px,9vw,52px);letter-spacing:5px;',
    '.fin-tit{font-family:\'Cinzel\',serif;font-size:clamp(22px,6vw,38px);letter-spacing:4px;'
)
c = c.replace(
    '.fin-sub{font-family:\'Cormorant Garamond\',serif;font-style:italic;font-size:clamp(20px,6vw,30px);',
    '.fin-sub{font-family:\'Cormorant Garamond\',serif;font-style:italic;font-size:clamp(15px,4.5vw,22px);'
)
c = c.replace(
    '#fin-frase{font-family:\'Cormorant Garamond\',serif;font-style:italic;font-size:clamp(18px,5.5vw,24px);color:rgba(255,255,255,.9);max-width:340px;line-height:1.9;margin-top:10px;',
    '#fin-frase{font-family:\'Cormorant Garamond\',serif;font-style:italic;font-size:clamp(14px,4vw,18px);color:rgba(255,255,255,.9);max-width:320px;line-height:1.7;margin-top:6px;'
)
c = c.replace(
    '#pant-final{display:none;position:fixed;inset:0;z-index:50;background:rgba(0,0,0,.93);align-items:center;justify-content:center;flex-direction:column;gap:14px;text-align:center;padding:40px;}',
    '#pant-final{display:none;position:fixed;inset:0;z-index:50;background:rgba(0,0,0,.93);align-items:center;justify-content:center;flex-direction:column;gap:8px;text-align:center;padding:24px;}'
)
print('3 pantalla final:', 'OK')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado OK')