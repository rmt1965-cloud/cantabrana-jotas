c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    "    cargarSello();\n",
    ""
)
c = c.replace(
    '.sello{position:absolute;bottom:-22px;right:10%;width:clamp(52px,13vw,72px);filter:drop-shadow(0 3px 12px rgba(140,20,20,.65));animation:sello-glow 3s ease-in-out infinite;}',
    '.sello{display:none;}'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')