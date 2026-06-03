c = open('index.html', 'r', encoding='utf-8').read()

# Mejorar textos splash
c = c.replace(
    'text-shadow:0 0 40px rgba(200,146,42,.9),0 0 80px rgba(200,146,42,.5),0 0 120px rgba(200,146,42,.3),0 0 200px rgba(200,146,42,.15);',
    'text-shadow:0 0 30px rgba(200,146,42,1),0 0 60px rgba(200,146,42,.7),0 0 100px rgba(200,146,42,.4);'
)

# Retazos de vida más brillante
c = c.replace(
    'font-size:clamp(22px,7vw,34px);color:rgba(200,146,42,.85);letter-spacing:3px;text-shadow:0 0 30px rgba(200,146,42,.7),0 0 60px rgba(200,146,42,.4);',
    'font-size:clamp(22px,7vw,34px);color:rgba(240,192,96,.95);letter-spacing:3px;text-shadow:0 0 30px rgba(200,146,42,1),0 0 60px rgba(200,146,42,.6);'
)

# Añadir líneas de luz dorada bajo Cantabrana y Retazos de vida
c = c.replace(
    '<div class="ld-titulo">Cantabrana</div>',
    '<div class="ld-titulo">Cantabrana</div>\n  <div style="width:180px;height:1px;background:linear-gradient(to right,transparent,rgba(200,146,42,.9),transparent);margin:4px auto;animation:ld-pulse 2s ease-in-out infinite;"></div>'
)
c = c.replace(
    'Retazos de Vida</div>',
    'Retazos de Vida</div>\n  <div style="width:140px;height:1px;background:linear-gradient(to right,transparent,rgba(200,146,42,.6),transparent);margin:2px auto;animation:ld-pulse 2.5s ease-in-out infinite;"></div>'
)

# Ken Burns en el fondo del splash - verificar que está activo
c = c.replace(
    "div.style.zIndex='5';",
    "div.style.zIndex='5';div.style.display='flex';"
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')