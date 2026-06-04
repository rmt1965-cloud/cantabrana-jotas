c = open('index.html', 'r', encoding='utf-8').read()

# Reemplazar iniciarAmbiente en arrancar por reproducción directa
c = c.replace(
    """  // Desbloquear audio en Android con elemento temporal
  const tmp = document.createElement('audio');
  tmp.src = 'data:audio/wav;base64,UklGRigAAABXQVZFZm10IBIAAAABAAEARKwAAIhYAQACABAAAABkYXRhAgAAAAEA';
  tmp.play().then(()=>{ tmp.remove(); iniciarAmbiente(); }).catch(()=>{ iniciarAmbiente(); });""",
    """  // Reproducir ambiente directamente en el gesto del usuario
  const idx = Math.floor(Math.random() * CFG.ambiente.length);
  aAmb.src = CFG.ambiente[idx];
  aAmb.volume = 0.35;
  aAmb.loop = true;
  const playPromise = aAmb.play();
  if (playPromise) playPromise.catch(()=>{});"""
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')