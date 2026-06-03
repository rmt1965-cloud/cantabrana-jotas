c = open('index.html', 'r', encoding='utf-8').read()

# Retazos de vida más grande
c = c.replace(
    'font-size:clamp(18px,5.5vw,28px);color:rgba(200,146,42,.7);letter-spacing:3px;',
    'font-size:clamp(22px,7vw,34px);color:rgba(200,146,42,.85);letter-spacing:3px;text-shadow:0 0 30px rgba(200,146,42,.7),0 0 60px rgba(200,146,42,.4);'
)

# Aura en Cantabrana
c = c.replace(
    'text-shadow:0 0 40px rgba(200,146,42,.9),0 0 80px rgba(200,146,42,.5);',
    'text-shadow:0 0 40px rgba(200,146,42,.9),0 0 80px rgba(200,146,42,.5),0 0 120px rgba(200,146,42,.3),0 0 200px rgba(200,146,42,.15);'
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')