import os, json
fotos = []
for i in range(1, 98):
    for ext in ['.jpg', '.JPG', '.png']:
        f = f'fotos/arcos/foto{str(i).zfill(3)}{ext}'
        if os.path.exists(f):
            fotos.append(f)
            break

c = open('index.html', 'r', encoding='utf-8').read()

# Reemplazar la funcion cargarFotos
old = """async function cargarFotos(){
  fotos = [];
  // Pedir 12 fotos en paralelo
  const promesas = Array(12).fill(0).map(() =>
    fetch(CFG.fotos_servidor).then(r=>r.json()).catch(()=>null)
  );
  const res = await Promise.all(promesas);
  const urls = res.filter(r=>r?.url).map(r=>r.url);
  fotos = [...new Set(urls)]; // sin duplicados
  if (!fotos.length) fotos = ['https://picsum.photos/1080/1920?random=' + Date.now()];
}"""

new = f"""async function cargarFotos(){{
  const lista = {json.dumps(fotos)};
  // Mezclar aleatoriamente
  fotos = lista.sort(() => Math.random() - 0.5);
}}"""

c = c.replace(old, new)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo -', len(fotos), 'fotos')