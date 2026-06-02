c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    """  // Mostrar botones
  document.getElementById('ui-bottom').classList.add('show');
  // Pantalla final despuÃ©s de 8s
  setTimeout(() => {
    document.getElementById('pant-repro').style.display = 'none';
    document.getElementById('pant-final').classList.add('show');
  }, 8000);""",
    """  // Mostrar portada y luego pantalla final
  clearTimeout(fotoTimer);
  const fotoFinal = document.getElementById('foto-img');
  const blurFinal = document.getElementById('foto-blur');
  const trans = document.getElementById('foto-trans');
  trans.classList.add('on');
  setTimeout(() => {
    fotoFinal.src = 'fotos/portada/portada1.png';
    blurFinal.style.backgroundImage = "url('fotos/portada/portada1.png')";
    fotoFinal.onload = () => {
      trans.classList.remove('on');
      fotoFinal.classList.add('show');
    };
  }, 500);
  document.getElementById('ui-bottom').classList.add('show');
  setTimeout(() => {
    document.getElementById('pant-repro').style.display = 'none';
    document.getElementById('pant-final').classList.add('show');
  }, 6000);"""
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')