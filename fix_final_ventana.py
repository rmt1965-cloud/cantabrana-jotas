c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    '<div class="fin-titulo">Cantabrana</div>\n  <div class="fin-subtitulo">La tradici&oacute;n vive en cada nota.<br>Gracias por escuchar.</div>',
    '''<div class="fin-titulo" style="font-size:clamp(24px,7vw,40px);">Cantabrana</div>
  <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(14px,4vw,20px);color:rgba(200,146,42,.8);letter-spacing:3px;margin-top:-8px;">Retazos de Historia</div>
  <div style="font-family:'Cinzel',serif;font-size:clamp(10px,2.8vw,13px);letter-spacing:4px;color:rgba(255,255,255,.45);text-transform:uppercase;margin-top:6px;">Rafael Molina Toledo</div>
  <div class="fin-subtitulo" style="font-size:clamp(15px,4.5vw,22px);margin-top:20px;">La tradici&oacute;n vive en cada nota,<br>en cada puerta, en cada arco de piedra...<br><br>Gracias por escuchar.</div>'''
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')