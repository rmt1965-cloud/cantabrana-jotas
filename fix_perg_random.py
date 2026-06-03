c = open('index.html', 'r', encoding='utf-8').read()

textos = [
    "Esto no es una grabaci\u00f3n.<br>Es memoria viva de Cantabrana.<br>Canciones de otra \u00e9poca,<br>algunas pueden herir tu sensibilidad.",
    "Esta voz perteneci\u00f3 a alguien de aqu\u00ed.<br>Son jotas de otro tiempo.<br>Algunas pueden herir tu sensibilidad.<br>Esch\u00fachalas con respeto.",
    "Cierra los ojos.<br>Lo que vas a escuchar es de otra \u00e9poca.<br>Puede herir tu sensibilidad.<br>Esc\u00fachalo. Vale la pena.",
    "Canta quien recuerda.<br>Estas jotas son de otro tiempo.<br>Algunas pueden herir tu sensibilidad.<br>Bienvenido a Cantabrana.",
    "Esto no debi\u00f3 olvidarse.<br>Son canciones de otra \u00e9poca.<br>Algunas pueden herir tu sensibilidad.<br>Ac\u00e9rcate con respeto.",
]

# Añadir JS para texto aleatorio del pergamino
js_perg = """
  // Texto aleatorio del pergamino
  const TEXTOS_PERG = """ + str(textos).replace("'", '"') + """;
  const idxPerg = crypto.getRandomValues(new Uint32Array(1))[0] % TEXTOS_PERG.length;
  document.querySelector('.aviso').innerHTML = TEXTOS_PERG[idxPerg];
"""

c = c.replace(
    '      // Sello real\n',
    js_perg + '\n      // Sello real\n'
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')