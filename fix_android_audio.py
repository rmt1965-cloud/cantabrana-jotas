c = open('index.html', 'r', encoding='utf-8').read()

c = c.replace(
    'function arrancar(){\n  if(window._arrancado) return;\n  window._arrancado = true;',
    """function arrancar(){
  if(window._arrancado) return;
  window._arrancado = true;
  // Desbloquear audio en Android con elemento temporal
  const tmp = document.createElement('audio');
  tmp.src = 'data:audio/wav;base64,UklGRigAAABXQVZFZm10IBIAAAABAAEARKwAAIhYAQACABAAAABkYXRhAgAAAAEA';
  tmp.play().then(()=>{ tmp.remove(); iniciarAmbiente(); }).catch(()=>{ iniciarAmbiente(); });"""
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')