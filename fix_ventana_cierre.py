with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Textos mas grandes en pantalla final
c = c.replace(
    ".fin-tit{font-family:'Cinzel',serif;font-size:clamp(22px,6vw,38px);letter-spacing:4px;",
    ".fin-tit{font-family:'Cinzel',serif;font-size:clamp(28px,8vw,48px);letter-spacing:5px;"
)
c = c.replace(
    ".fin-sub{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(15px,4.5vw,22px);",
    ".fin-sub{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(18px,5.5vw,28px);"
)
c = c.replace(
    "#fin-frase{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(14px,4vw,18px);color:rgba(255,255,255,.9);max-width:320px;line-height:1.7;margin-top:6px;",
    "#fin-frase{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(17px,5vw,22px);color:rgba(255,255,255,.9);max-width:360px;line-height:1.8;margin-top:10px;"
)
c = c.replace(
    ".fin-aut{font-family:'Cinzel',serif;font-size:clamp(11px,3vw,14px);",
    ".fin-aut{font-family:'Cinzel',serif;font-size:clamp(12px,3.2vw,15px);"
)
print('OK textos mas grandes')

# Frase estatica HTML vacía para que no se vea antes del JS
c = c.replace(
    '<div id="fin-frase">La tradic&oacute;n vive en cada nota,<br>entre puertas y arcos de piedra.<br><br>Gracias por escuchar.</div>',
    '<div id="fin-frase"></div>'
)
print('OK frase estatica vaciada')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')