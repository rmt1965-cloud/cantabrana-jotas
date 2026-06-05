with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Portada visible mas tiempo: 4s -> 8s antes de la despedida
c = c.replace(
    "  // Despedida tras 4s\n  setTimeout(()=>{",
    "  // Despedida tras 8s\n  setTimeout(()=>{"
)
c = c.replace(
    "document.getElementById('pant-repro').style.display='none';",
    "document.getElementById('pant-repro').style.display='none';"
)

# El timeout de 4000 -> 8000
c = c.replace(
    "mostrarDespedida(()=>{\n      // Frase final aleatoria",
    "mostrarDespedida(()=>{\n      // Frase final aleatoria"
)

# Buscar el setTimeout de 4000 en finJota
import re
m = re.search(r"(// Despedida tras \ds\s*\n\s*setTimeout\(\(\)=>\{.*?pant-repro.*?display.*?'none';.*?\},)(\d+)\)", c, re.DOTALL)
if m:
    c = c[:m.start(2)] + '8000' + c[m.end(2):]
    print('OK portada visible 8s')
else:
    print('WARN no encontrado con regex')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')