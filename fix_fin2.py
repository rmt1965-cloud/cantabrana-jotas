c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'let fotoTimer = null;',
    'let fotoTimer = null;\nlet jotaFinalizada = false;'
)
c = c.replace(
    'function finJota(){',
    """function finJota(){
  if (jotaFinalizada) return;
  jotaFinalizada = true;"""
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')