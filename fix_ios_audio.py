c = open('index.html', 'r', encoding='utf-8').read()

# En arrancar, usar AudioContext para desbloquear iOS
c = c.replace(
    'function arrancar(){\n  if(window._arrancado) return;\n  window._arrancado = true;\n  iniciarAmbiente();',
    '''function arrancar(){
  if(window._arrancado) return;
  window._arrancado = true;
  // Desbloquear AudioContext en iOS
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    ctx.resume();
  } catch(e){}
  iniciarAmbiente();'''
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')