with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Titulo: 28-44px -> 22-36px
c = c.replace(
    'font-size:clamp(28px,8vw,44px);letter-spacing:8px;',
    'font-size:clamp(22px,6vw,36px);letter-spacing:6px;'
)

# Subtitulo: 18-28px -> 15-24px
c = c.replace(
    'font-size:clamp(18px,5.5vw,28px);color:rgba(240,192,96,.95);letter-spacing:3px;',
    'font-size:clamp(15px,4.5vw,22px);color:rgba(240,192,96,.95);letter-spacing:3px;'
)

# Reducir gap del loading
c = c.replace(
    'flex-direction:column;gap:16px;',
    'flex-direction:column;gap:10px;'
)

# Reducir lineas
c = c.replace('width:180px;height:1px;', 'width:140px;height:1px;')
c = c.replace('width:140px;height:1px;background:linear-gradient(to right,transparent,rgba(200,146,42,.6)', 'width:110px;height:1px;background:linear-gradient(to right,transparent,rgba(200,146,42,.6)')

print("OK")
open('index.html', 'w', encoding='utf-8').write(c)
print("Guardado")