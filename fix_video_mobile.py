c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    '<video id="vid" src="video/inicio.mp4" playsinline muted>',
    '<video id="vid" src="" playsinline muted webkit-playsinline>'
)
c = c.replace(
    '<video id="vid-final" src="" playsinline muted>',
    '<video id="vid-final" src="" playsinline muted webkit-playsinline>'
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')