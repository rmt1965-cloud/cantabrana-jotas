c = open('index.html', 'r', encoding='utf-8').read()

# Añadir "toca para comenzar" en el loading
c = c.replace(
    '<div class="ld-linea"></div>\n</div>',
    '''<div class="ld-linea"></div>
  <div id="ld-toca" style="font-family:'Cinzel',serif;font-size:clamp(9px,2.5vw,12px);letter-spacing:3px;color:rgba(200,146,42,.6);text-transform:uppercase;margin-top:16px;animation:ld-pulse 1.8s ease-in-out infinite;opacity:0;transition:opacity 1s ease;">&#10022; Toca para comenzar &#10022;</div>
</div>'''
)

# Hacer que el loading espere un toque
c = c.replace(
    "  // Ocultar loading\n  setTimeout(() => {\n    document.getElementById('loading').classList.add('fade');",
    """  // Mostrar 'toca para comenzar' tras 1.5s
  setTimeout(() => {
    document.getElementById('ld-toca').style.opacity = '1';
  }, 1500);

  // Esperar toque del usuario para iniciar audio y continuar
  await new Promise(resolve => {
    const el = document.getElementById('loading');
    const handler = () => { el.removeEventListener('click', handler); el.removeEventListener('touchend', handler); resolve(); };
    el.addEventListener('click', handler);
    el.addEventListener('touchend', handler);
  });

  // Iniciar ambiente tras interaccion
  iniciarAmbiente();

  // Ocultar loading
  setTimeout(() => {
    document.getElementById('loading').classList.add('fade');"""
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')