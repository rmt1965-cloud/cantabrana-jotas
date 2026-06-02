c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    '<img id="sello-final" src="" alt="Sello" style="width:clamp(80px,20vw,130px);margin-top:16px;filter:drop-shadow(0 4px 16px rgba(140,20,20,.7));animation:sello-glow 3s ease-in-out infinite;mix-blend-mode:screen;">',
    ''
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')