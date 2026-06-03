import os, json, re

# Fotos extra sin nombres feos
fotos_intro = []
for f in sorted(os.listdir('fotos/extra')):
    if f.lower().endswith(('.jpg','.jpeg','.png')) and not f.startswith('.') and 'ChatGPT' not in f:
        fotos_intro.append('fotos/extra/' + f)
for f in ['rustico1.jpg','rustico2.jpg','rustico3.jpg','rustico4.jpg']:
    fotos_intro.append('video/intro/' + f)

# Ventanas fijas
VENTANAS_FIJAS = [
    {"src": "fotos/ventanas/ventana1.jpg", "leyenda": "Cantabrana llama al pasado"},
    {"src": "fotos/ventanas/ventana3.jpg", "leyenda": "a trav\u00e9s de sus ventanas"},
    {"src": "fotos/ventanas/ventana4.png", "leyenda": "sus arcos y sus puertas centenarias"},
]

c = open('index.html', 'r', encoding='utf-8').read()

# 1. Pool intro sin ChatGPT
c = re.sub(
    r'const FOTOS_POOL = \[.*?\];',
    'const FOTOS_POOL = ' + json.dumps(fotos_intro) + ';',
    c, flags=re.DOTALL
)

# 2. Ventanas: mezclar 3 aleatorias con 3 fijas y elegir 3 total
c = c.replace(
    """  const frasesAleatorias = cryptoShuffle(FRASES_POOL).slice(0,3);
  const fotosAleatorias = cryptoShuffle(FOTOS_POOL).slice(0,3);
  
  CFG.ventanas = [
    { src: fotosAleatorias[0], leyenda: frasesAleatorias[0] },
    { src: fotosAleatorias[1], leyenda: frasesAleatorias[1] },
    { src: fotosAleatorias[2], leyenda: frasesAleatorias[2] },
    { src: 'fotos/ventanas/ventana1.jpg', leyenda: 'Cantabrana llama al pasado' },
    { src: 'fotos/ventanas/ventana3.jpg', leyenda: 'a trav\u00e9s de sus ventanas' },
    { src: 'fotos/ventanas/ventana4.png', leyenda: 'sus arcos y sus puertas centenarias' },
  ];""",
    """  const frasesAleatorias = cryptoShuffle(FRASES_POOL);
  const fotosAleatorias = cryptoShuffle(FOTOS_POOL);
  
  // 3 ventanas aleatorias del pool
  const ventanasAleatorias = fotosAleatorias.slice(0,3).map((src,i) => ({
    src, leyenda: frasesAleatorias[i]
  }));
  
  // Mezclar con las 3 fijas y elegir 3 en total
  const todasVentanas = cryptoShuffle([...ventanasAleatorias, ...""" + json.dumps(VENTANAS_FIJAS, ensure_ascii=False) + """]);
  CFG.ventanas = todasVentanas.slice(0,3);"""
)

# 3. Botones más cálidos
c = c.replace(
    '&#8635; Reiniciar',
    '&#9834; Escuchar otra jota'
)
c = c.replace(
    'Salir &#10005;',
    'Hasta pronto &#10022;'
)
c = c.replace(
    '&#8635; Escuchar otra jota',
    '&#9834; Escuchar otra jota'
)

# 4. Ticker opción D - barra dorada fondo oscuro texto negro visible
c = c.replace(
    '#ticker{position:fixed;bottom:52px;left:0;right:0;z-index:30;overflow:hidden;height:18px;}',
    '#ticker{position:fixed;bottom:52px;left:0;right:0;z-index:30;overflow:hidden;height:28px;background:rgba(200,146,42,.85);}'
)
c = c.replace(
    '#ticker-in{display:inline-block;white-space:nowrap;padding-left:100%;font-family:\'Cinzel\',serif;font-size:9px;letter-spacing:2px;color:rgba(200,146,42,.65);text-transform:uppercase;animation:ticker 22s linear infinite;}',
    '#ticker-in{display:inline-block;white-space:nowrap;padding-left:100%;font-family:\'Cinzel\',serif;font-size:11px;letter-spacing:2px;color:#000;text-transform:uppercase;animation:ticker 22s linear infinite;font-weight:700;line-height:28px;}'
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')