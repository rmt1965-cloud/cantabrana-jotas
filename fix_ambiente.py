c = open('index.html', 'r', encoding='utf-8').read()

# Añadir lista de ambiente al CFG
c = c.replace(
    "  jotas_url: 'audio/',",
    """  jotas_url: 'audio/',
  ambiente: ['audio/ambiente/ambiente10.mp3','audio/ambiente/ambiente11.mp3','audio/ambiente/ambiente14.mp3','audio/ambiente/ambiente15.mp3','audio/ambiente/ambiente17.mp3'],"""
)

# Cargar ambiente local
c = c.replace(
    "  // Mantener pantalla encendida",
    """  // Cargar música ambiente local
  const ambIdx = Math.floor(Math.random() * CFG.ambiente.length);
  aAmb.src = CFG.ambiente[ambIdx];
  aAmb.volume = 0;
  aAmb.loop = true;
  aAmb.play().catch(()=>{});
  // Fade in suave
  let vol = 0;
  const fadeIn = setInterval(() => {
    vol = Math.min(vol + 0.02, 0.45);
    aAmb.volume = vol;
    if (vol >= 0.45) clearInterval(fadeIn);
  }, 100);

  // Mantener pantalla encendida"""
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')