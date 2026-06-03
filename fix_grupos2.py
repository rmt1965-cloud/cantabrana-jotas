import json, re
c = open('index.html', 'r', encoding='utf-8').read()

c = c.replace(
    """  // 3 ventanas aleatorias del pool
  const ventanasAleatorias = fotosAleatorias.slice(0,3).map((src,i) => ({
    src, leyenda: frasesAleatorias[i]
  }));
  // Mezclar con las 3 fijas y elegir 3 en total
  const todasVentanas = cryptoShuffle([...ventanasAleatorias, ...[{"src": "fotos/ventanas/ventana1.jpg", "leyenda": "Cantabrana llama al pasado"}, {"src": "fotos/ventanas/ventana3.jpg", "leyenda": "a trav\\u00e9s de sus ventanas"}, {"src": "fotos/ventanas/ventana4.png", "leyenda": "sus arcos y sus puertas centenarias"}]]);
  CFG.ventanas = todasVentanas.slice(0,3);""",
    """  // 3 fotos aleatorias con el grupo de frases integro en orden
  CFG.ventanas = [
    { src: fotosAleatorias[0], leyenda: frasesAleatorias[0] },
    { src: fotosAleatorias[1], leyenda: frasesAleatorias[1] },
    { src: fotosAleatorias[2], leyenda: frasesAleatorias[2] },
  ];"""
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')