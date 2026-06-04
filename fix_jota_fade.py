with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Jota sube lentamente desde 0 hasta volumen 1 en ~3s
old = "aJota.src=CFG.jotas_url+encodeURIComponent(jota.a);\n  aJota.load();aJota.volume=1;\n  mostrarFoto(0);\n  aJota.play().catch(e=>console.warn(e));"
new = "aJota.src=CFG.jotas_url+encodeURIComponent(jota.a);\n  aJota.load();aJota.volume=0;\n  mostrarFoto(0);\n  aJota.play().catch(e=>console.warn(e));\n  let vj=0;const fj=setInterval(()=>{vj=Math.min(vj+0.008,1);aJota.volume=vj;if(vj>=1)clearInterval(fj);},60);"

if old in c:
    c = c.replace(old, new)
    print("OK fade jota")
else:
    print("WARN no encontrado")

open('index.html', 'w', encoding='utf-8').write(c)
print("Guardado")