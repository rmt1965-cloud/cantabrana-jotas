c = open('index.html', 'r', encoding='utf-8').read()

# Cambiar Retazos de historia por Retazos de vida y más grande
c = c.replace(
    'Retazos de Historia',
    'Retazos de Vida'
)
c = c.replace(
    'font-size:clamp(14px,4vw,20px);color:rgba(200,146,42,.8);letter-spacing:3px;margin-top:-8px;',
    'font-size:clamp(20px,6vw,30px);color:rgba(200,146,42,.9);letter-spacing:3px;margin-top:-4px;text-shadow:0 0 20px rgba(200,146,42,.5);'
)

# Título Cantabrana más grande
c = c.replace(
    '<div class="fin-titulo" style="font-size:clamp(24px,7vw,40px);">Cantabrana</div>',
    '<div class="fin-titulo" style="font-size:clamp(30px,9vw,52px);text-shadow:0 0 40px rgba(200,146,42,.6);">Cantabrana</div>'
)

# Frase y Gracias más grandes
c = c.replace(
    'font-size:clamp(15px,4.5vw,22px);margin-top:20px;',
    'font-size:clamp(18px,5.5vw,26px);margin-top:20px;line-height:2.0;'
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')