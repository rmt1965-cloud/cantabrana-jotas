c = open('index.html', 'r', encoding='utf-8').read()

# Texto en 4 líneas
c = c.replace(
    'Estas canciones son de otra época,<br>algunas pueden herir su sensibilidad',
    'Estas canciones<br>son de otra época,<br>algunas pueden herir<br>su sensibilidad'
)

# Tamaño grande
c = c.replace(
    'font-size:clamp(12px,3.5vw,17px);',
    'font-size:clamp(18px,5.5vw,26px);font-weight:700;'
)

# Ancho mayor
c = c.replace(
    'width:68%;',
    'width:80%;'
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')