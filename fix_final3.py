import re
c = open('index.html', 'r', encoding='utf-8').read()

# Botón volver al inicio
c = c.replace(
    '&#9834; Escuchar otra jota',
    '&#8635; Volver al inicio'
)

# Frases aleatorias en la ventana final
js_frase = """
  // Frase aleatoria ventana final
  const FRASES_FINAL = [
    'La tradici\u00f3n vive en cada nota, en las puertas y en los arcos de piedra.',
    'La tradici\u00f3n vive en cada nota, en las puertas centenarias y en los arcos de piedra.',
    'La tradici\u00f3n vive en cada nota, entre puertas y arcos de piedra.',
    'La tradici\u00f3n vive en la m\u00fasica, en las puertas y en los arcos de piedra.',
    'La tradici\u00f3n late en cada nota, en las puertas y en los arcos milenarios.',
  ];
  const idxFF = crypto.getRandomValues(new Uint32Array(1))[0] % FRASES_FINAL.length;
  document.getElementById('frase-final').innerHTML = FRASES_FINAL[idxFF] + '<br><br>Gracias por escuchar.';
"""

# Añadir JS antes de mostrar pantalla final
c = c.replace(
    "      document.getElementById('pant-final').classList.add('show');",
    js_frase + "\n      document.getElementById('pant-final').classList.add('show');"
)

# Hacer frase más visible
c = c.replace(
    'font-size:clamp(18px,5.5vw,26px);margin-top:20px;line-height:2.0;',
    'font-size:clamp(20px,6vw,28px);margin-top:20px;line-height:1.9;color:rgba(255,255,255,.9);text-shadow:0 0 20px rgba(200,146,42,.3);'
)

# Añadir id a la frase final
c = c.replace(
    "<div class=\"fin-frase\"",
    "<div id=\"frase-final\" class=\"fin-frase\""
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')