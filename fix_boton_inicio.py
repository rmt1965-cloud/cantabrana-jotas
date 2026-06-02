c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'animation:ld-pulse 1.8s ease-in-out infinite;opacity:0;transition:opacity 1s ease;padding:12px 28px;border:1px solid rgba(200,146,42,.5);border-radius:2px;cursor:pointer;background:rgba(0,0,0,.4);',
    'animation:ld-pulse 1.8s ease-in-out infinite;opacity:0;transition:opacity 1s ease;padding:18px 48px;border:2px solid rgba(200,146,42,.7);border-radius:4px;cursor:pointer;background:rgba(200,146,42,.15);font-size:clamp(13px,4vw,18px);letter-spacing:4px;min-width:220px;'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')