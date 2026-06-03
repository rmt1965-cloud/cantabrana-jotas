import json, re

GRUPOS = [
    ["Cantabrana llama al pasado", "a trav\u00e9s de sus ventanas", "sus arcos y sus puertas centenarias"],
    ["Aqu\u00ed vivieron tus ancestros", "Aqu\u00ed son\u00f3 esta m\u00fasica por primera vez", "Ahora te toca a ti escucharla"],
    ["Siglos de historia en tres minutos", "Esto no es nostalgia. Es identidad.", "Bienvenido a Cantabrana"],
    ["Algunas puertas nunca se cerraron del todo", "Detr\u00e1s hay voces que esperaban ser escuchadas", "Esta es una de ellas"],
    ["Lo que somos viene de donde venimos", "Cantabrana no es un lugar, es una ra\u00edz", "Y esa ra\u00edz eres t\u00fa"],
]

c = open('index.html', 'r', encoding='utf-8').read()

nuevo = """  // Elegir grupo aleatorio de frases
  const GRUPOS_FRASES = """ + json.dumps(GRUPOS, ensure_ascii=False) + """;
  const idxGrupo = crypto.getRandomValues(new Uint32Array(1))[0] % GRUPOS_FRASES.length;
  const grupoElegido = GRUPOS_FRASES[idxGrupo];
  
  const frasesAleatorias = grupoElegido;
  const fotosAleatorias = cryptoShuffle(FOTOS_POOL);"""

c = re.sub(
    r'const frasesAleatorias = cryptoShuffle\(FRASES_POOL\);\n  const fotosAleatorias = cryptoShuffle\(FOTOS_POOL\);',
    nuevo,
    c
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')