c = open('index.html', 'r', encoding='utf-8').read()

# Añadir función arrancar
c = c.replace(
    'async function init(){',
    """function arrancar(){
  if(window._arrancado) return;
  window._arrancado = true;
  if(window._resolve) window._resolve();
}

async function init(){"""
)

# Añadir onclick al botón
c = c.replace(
    '<div id="ld-btn">Pulsar para iniciar</div>',
    '<div id="ld-btn" onclick="arrancar()" ontouchstart="arrancar()">Pulsar para iniciar</div>'
)

# Guardar _resolve
c = c.replace(
    """  await new Promise(resolve=>{
    const el=document.getElementById('loading');
    const h=()=>{el.removeEventListener('click',h);el.removeEventListener('touchend',h);el.removeEventListener('touchstart',h);resolve();};
    el.addEventListener('click',h);el.addEventListener('touchend',h);el.addEventListener('touchstart',h);
  });""",
    """  await new Promise(resolve=>{
    window._resolve = resolve;
    const el=document.getElementById('loading');
    const h=()=>{el.removeEventListener('click',h);el.removeEventListener('touchend',h);resolve();};
    el.addEventListener('click',h);el.addEventListener('touchend',h);
  });"""
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')