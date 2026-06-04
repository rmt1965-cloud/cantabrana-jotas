with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# El pergamino desaparece y 5s despues arranca la jota - hacerlo mas suave
# Añadir transition al pergamino y alargar el fade out
old = "document.getElementById('pant-perg').style.opacity='0';"
new = "const perg=document.getElementById('pant-perg');perg.style.transition='opacity 2s ease';perg.style.opacity='0';"

if old in c:
    c = c.replace(old, new)
    print("OK fade pergamino suave")
else:
    print("WARN no encontrado")

# La jota arranca a los 5s del pergamino - añadir fade in del reproductor
old2 = "document.getElementById('pant-repro').classList.add('show');"
new2 = "const pr=document.getElementById('pant-repro');pr.style.opacity='0';pr.classList.add('show');pr.style.transition='opacity 1.5s ease';setTimeout(()=>{pr.style.opacity='1';},50);"

if old2 in c:
    c = c.replace(old2, new2)
    print("OK fade in reproductor")
else:
    print("WARN reproductor no encontrado")

open('index.html', 'w', encoding='utf-8').write(c)
print("Guardado")