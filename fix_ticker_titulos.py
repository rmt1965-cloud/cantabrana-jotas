import pandas as pd
import re

df = pd.read_excel('Jotas_y_canciones_autores.xlsx')
mapa = {}
for _, row in df.iterrows():
    num = int(row['Nº'])
    titulo = str(row['descripción']).strip()
    mapa[num] = titulo

print("Jotas en excel:", len(mapa))

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

def añadir_titulo(match):
    obj = match.group(0)
    m = re.search(r'--(\d+)\.mp3', obj)
    if not m:
        m = re.search(r'-(\d+)\.mp3', obj)
    if m:
        num = int(m.group(1))
        if num in mapa and ',t:' not in obj:
            titulo = mapa[num].replace("'", "\\'")
            obj = obj.rstrip('}') + ",t:'" + titulo + "'}"
    return obj

new_c = re.sub(r"\{a:'[^']+\.mp3',[^}]+\}", añadir_titulo, c)
cambios = new_c.count(",t:'") - c.count(",t:'")
print(f"Titulos añadidos: {cambios}")

# Ticker muestra: TITULO · Cantante
old_t = "document.getElementById('ticker-in').textContent='\u266a  '+jota.c+' \xb7 '+jota.m+' \xb7 Cantabrana \xb7 Retazos de Vida  \u266a';"
new_t = "document.getElementById('ticker-in').textContent='\u266a  '+(jota.t||jota.c)+' \xb7 '+jota.c+' \xb7 Cantabrana  \u266a';"

if old_t in new_c:
    new_c = new_c.replace(old_t, new_t)
    print("OK ticker con titulo")
else:
    print("WARN ticker — buscar manualmente")

open('index.html', 'w', encoding='utf-8').write(new_c)
print("Guardado OK")