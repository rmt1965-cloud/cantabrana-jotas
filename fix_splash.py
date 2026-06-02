c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    '<div class="ld-titulo">Cantabrana</div>',
    '''<div class="ld-titulo">Cantabrana</div>
  <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(14px,4vw,20px);color:rgba(200,146,42,.7);letter-spacing:3px;margin-top:-8px;">Retazos de Vida</div>
  <div style="font-family:'Cinzel',serif;font-size:clamp(10px,2.8vw,14px);letter-spacing:4px;color:rgba(255,255,255,.4);text-transform:uppercase;margin-top:4px;">Rafael Molina Toledo</div>'''
)
c = c.replace(
    '&#10022; Toca para comenzar &#10022;',
    'Pulsar para iniciar'
)
c = c.replace(
    "animation:ld-pulse 1.8s ease-in-out infinite;opacity:0;transition:opacity 1s ease;",
    "animation:ld-pulse 1.8s ease-in-out infinite;opacity:0;transition:opacity 1s ease;padding:12px 28px;border:1px solid rgba(200,146,42,.5);border-radius:2px;cursor:pointer;background:rgba(0,0,0,.4);"
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')