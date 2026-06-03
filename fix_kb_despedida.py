c = open('index.html', 'r', encoding='utf-8').read()

# Añadir animación Ken Burns a la foto de despedida
c = c.replace(
    '#desp-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0.6;}',
    '#desp-img{position:absolute;inset:-10%;width:120%;height:120%;object-fit:cover;opacity:0.6;animation:kenburns1 8s ease-in-out forwards;}'
)

# Elegir animación aleatoria
c = c.replace(
    "  img.src = VISTAS[idxV];",
    """  const KB_ANIMS = ['kenburns1','kenburns2','kenburns3','kenburns4'];
  const idxKB = crypto.getRandomValues(new Uint32Array(1))[0] % KB_ANIMS.length;
  img.style.animation = KB_ANIMS[idxKB] + ' 8s ease-in-out forwards';
  img.src = VISTAS[idxV];"""
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')