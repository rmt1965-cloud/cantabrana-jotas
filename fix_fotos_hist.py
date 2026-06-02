c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    """  for(let i=todas.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[todas[i],todas[j]]=[todas[j],todas[i]];}
  fotos=todas;""",
    """  // Historial de fotos vistas - evitar repetir
  let histFotos=[];
  try{histFotos=JSON.parse(localStorage.getItem('cantabrana_fotos')||'[]');}catch(e){}
  // Fotos no vistas
  let noVistas=todas.filter(f=>!histFotos.includes(f));
  // Si ya las vio todas, resetear
  if(noVistas.length<10){histFotos=[];noVistas=todas;}
  // Fisher-Yates sobre no vistas
  for(let i=noVistas.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[noVistas[i],noVistas[j]]=[noVistas[j],noVistas[i]];}
  fotos=noVistas;
  // Guardar las que se van a ver en el historial
  const nuevasVistas=[...histFotos,...fotos.slice(0,20)].slice(-97);
  try{localStorage.setItem('cantabrana_fotos',JSON.stringify(nuevasVistas));}catch(e){}"""
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')