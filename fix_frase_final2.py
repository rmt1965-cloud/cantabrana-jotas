c = open('index.html', 'r', encoding='utf-8').read()

js = """
  // Frase aleatoria ventana final
  const FRASES_FINAL = [
    'La tradici\u00f3n vive en cada nota, en las puertas y en los arcos de piedra.',
    'La tradici\u00f3n vive en cada nota, en las puertas centenarias y en los arcos de piedra.',
    'La tradici\u00f3n vive en cada nota, entre puertas y arcos de piedra.',
    'La tradici\u00f3n vive en la m\u00fasica, en las puertas y en los arcos de piedra.',
    'La tradici\u00f3n late en cada nota, en las puertas y en los arcos milenarios.',
  ];
  const idxFF = crypto.getRandomValues(new Uint32Array(1))[0] % FRASES_FINAL.length;
  const elFrase = document.getElementById('frase-final');
  if (elFrase) elFrase.innerHTML = FRASES_FINAL[idxFF] + '<br><br>Gracias por escuchar.';
"""

c = c.replace(
    "      document.getElementById('pant-final').classList.add('show');",
    js + "\n      document.getElementById('pant-final').classList.add('show');"
)

# Añadir id a la frase final si no existe
if 'id="frase-final"' not in c:
    c = c.replace(
        '<div class="fin-frase"',
        '<div id="frase-final" class="fin-frase"'
    )

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')