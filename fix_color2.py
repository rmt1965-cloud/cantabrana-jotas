c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    'document.getElementById(\'perg-img\').src = pergUrl;',
    """document.getElementById('perg-img').src = pergUrl;
  if (pergUrl.includes('pergamino02')) {
    document.querySelector('.aviso').style.color = 'rgba(245,235,220,.95)';
    document.querySelector('.toca').style.color = 'rgba(220,200,160,.8)';
  } else {
    document.querySelector('.aviso').style.color = 'rgba(120,10,10,.92)';
    document.querySelector('.toca').style.color = 'rgba(100,5,5,.75)';
  }"""
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')