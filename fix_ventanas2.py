import os, json, re

# Pool completo de frases
FRASES = [
    # Grupo C
    "Aquí vivieron tus ancestros",
    "Aquí sonó esta música por primera vez",
    "Ahora te toca a ti escucharla",
    # Grupo E
    "Este silencio también es Cantabrana",
    "Aquí el tiempo no corre, respira",
    "Escucha lo que las piedras guardan",
    # Grupo F
    "Antes que tú, otros miraron estas piedras",
    "Las mismas jotas, las mismas voces",
    "La historia no termina, continúa",
    # Grupo G
    "Huele a piedra mojada y a memoria",
    "El eco de estas calles aún resuena",
    "Cierra los ojos. Ya estás aquí.",
    # Grupo H
    "Lo que somos viene de donde venimos",
    "Cantabrana no es un lugar, es una raíz",
    "Y esa raíz eres tú",
    # Grupo I
    "Algunas puertas nunca se cerraron del todo",
    "Detrás hay voces que esperaban ser escuchadas",
    "Esta es una de ellas",
    # Grupo J
    "Siglos de historia en tres minutos",
    "Esto no es nostalgia. Es identidad.",
    "Bienvenido a Cantabrana",
    # Grupo K
    "No hay prisa aquí",
    "El patrimonio no se visita, se siente",
    "Tómate un momento. Vale la pena.",
    # Grupo L
    "¿Cuántas generaciones caben en una jota?",
    "Las piedras recuerdan lo que los hombres olvidan",
    "Cantabrana te lo recuerda hoy",
]

# Fotos disponibles para las 3 aleatorias
fotos_pool = []
for carpeta in ['fotos/arcos', 'fotos/extra']:
    for f in sorted(os.listdir(carpeta)):
        if f.lower().endswith(('.jpg','.jpeg','.png')) and not f.startswith('.'):
            fotos_pool.append(carpeta + '/' + f)

c = open('index.html', 'r', encoding='utf-8').read()

# Nuevo array de ventanas con 3 aleatorias + 3 fijas
nuevo_ventanas = f"""
  // Ventanas con fotos y frases aleatorias
  const FRASES_POOL = {json.dumps(FRASES, ensure_ascii=False)};
  const FOTOS_POOL = {json.dumps(fotos_pool)};
  
  // Shuffle criptográfico
  function cryptoShuffle(arr) {{
    const a = [...arr];
    for(let i=a.length-1;i>0;i--){{
      const j=crypto.getRandomValues(new Uint32Array(1))[0]%(i+1);
      [a[i],a[j]]=[a[j],a[i]];
    }}
    return a;
  }}
  
  const frasesAleatorias = cryptoShuffle(FRASES_POOL).slice(0,3);
  const fotosAleatorias = cryptoShuffle(FOTOS_POOL).slice(0,3);
  
  CFG.ventanas = [
    {{ src: fotosAleatorias[0], leyenda: frasesAleatorias[0] }},
    {{ src: fotosAleatorias[1], leyenda: frasesAleatorias[1] }},
    {{ src: fotosAleatorias[2], leyenda: frasesAleatorias[2] }},
    {{ src: 'fotos/ventanas/ventana1.jpg', leyenda: 'Cantabrana llama al pasado' }},
    {{ src: 'fotos/ventanas/ventana3.jpg', leyenda: 'a través de sus ventanas' }},
    {{ src: 'fotos/ventanas/ventana4.png', leyenda: 'sus arcos y sus puertas centenarias' }},
  ];
"""

# Insertar antes de await mostrarVentanas
c = c.replace(
    '    await mostrarVentanas();',
    nuevo_ventanas + '\n    await mostrarVentanas();'
)

open('index.html', 'w', encoding='utf-8').write(c)
print(f'Listo - {len(FRASES)} frases, {len(fotos_pool)} fotos en pool')