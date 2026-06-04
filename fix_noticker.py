with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. CSS: eliminar ticker, añadir estilo titulo-jota
c = c.replace(
    "#ticker{position:fixed;bottom:52px;left:0;right:0;z-index:30;overflow:hidden;height:28px;background:rgba(200,146,42,.85);}",
    ""
)
c = c.replace(
    "#ticker-in{display:inline-block;white-space:nowrap;padding-left:100%;font-family:'Cinzel',serif;font-size:11px;letter-spacing:2px;color:#000;text-transform:uppercase;animation:ticker 22s linear infinite;font-weight:700;line-height:28px;}",
    ""
)
c = c.replace(
    "@keyframes ticker{0%{transform:translateX(0)}100%{transform:translateX(-100%)}}",
    ""
)

# Añadir CSS titulo-jota bajo municipio
c = c.replace(
    ".municipio{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(12px,3.2vw,16px);color:var(--gold);margin-top:3px;}",
    ".municipio{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(12px,3.2vw,16px);color:var(--gold);margin-top:3px;}\n.titulo-jota{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(13px,3.5vw,18px);color:rgba(240,192,96,.75);margin-top:5px;letter-spacing:1px;opacity:0;transition:opacity 1.5s ease;}"
)
print('OK CSS ticker eliminado, titulo-jota añadido')

# 2. HTML: eliminar div ticker, añadir div titulo-jota
c = c.replace(
    '<div id="ticker"><span id="ticker-in">&#9834; Cantabrana &middot; Retazos de Vida &middot; Patrimonio Musical &#9834;</span></div>',
    ''
)
c = c.replace(
    '      <div class="municipio" id="municipio">Cantabrana</div>',
    '      <div class="municipio" id="municipio">Cantabrana</div>\n      <div class="titulo-jota" id="titulo-jota"></div>'
)
print('OK HTML ticker eliminado, titulo-jota añadido')

# 3. JS: actualizar titulo-jota en lugar de ticker
c = c.replace(
    "document.getElementById('ticker-in').textContent='♪  '+(jota.t||jota.c)+' · '+jota.c+' · Cantabrana  ♪';",
    "const tj=document.getElementById('titulo-jota');tj.textContent=jota.t||jota.c;setTimeout(()=>{tj.style.opacity='1';},800);"
)
print('OK JS ticker->titulo-jota')

# 4. JS: en finJota ocultar titulo-jota en lugar de ticker
c = c.replace(
    "document.getElementById('ticker').style.display='none';",
    "document.getElementById('titulo-jota').style.opacity='0';"
)
print('OK JS ocultar titulo-jota al fin')

# 5. Ajustar prog (barra progreso) que estaba encima del ticker
c = c.replace(
    '#prog{position:fixed;bottom:76px;left:20px;right:20px;z-index:30;}',
    '#prog{position:fixed;bottom:56px;left:20px;right:20px;z-index:30;}'
)
print('OK prog ajustado')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado OK')