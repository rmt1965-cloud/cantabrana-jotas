c = open('index.html', 'r', encoding='utf-8').read()

# Retazos de vida más grande
c = c.replace(
    'font-size:clamp(14px,4vw,20px);color:rgba(200,146,42,.7);letter-spacing:3px;',
    'font-size:clamp(18px,5.5vw,28px);color:rgba(200,146,42,.7);letter-spacing:3px;'
)

# Leyendas de ventanas
c = c.replace(
    "leyenda: 'Cantabrana llama a su pasado'",
    "leyenda: 'Cantabrana llama al pasado'"
)
c = c.replace(
    "leyenda: 'a trav\\u00e9s de sus puertas'",
    "leyenda: 'a trav\\u00e9s de sus ventanas'"
)
c = c.replace(
    "leyenda: 'centenarias'",
    "leyenda: 'sus arcos y sus puertas centenarias'"
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')