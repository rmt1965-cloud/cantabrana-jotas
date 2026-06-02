c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    '  aJota.onended = finJota;',
    """  aJota.onended = finJota;
  aJota.addEventListener('loadedmetadata', () => {
    const dur = aJota.duration;
    if (dur && isFinite(dur)) {
      setTimeout(finJota, (dur + 1) * 1000);
    }
  });"""
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')