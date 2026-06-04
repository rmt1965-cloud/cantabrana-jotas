with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Ocultar ui-bot cuando arranca finJota
old = "function finJota(){\n  if(jotaFin)return;jotaFin=true;"
new = "function finJota(){\n  if(jotaFin)return;jotaFin=true;\n  document.getElementById('ui-bot').style.opacity='0';\n  document.getElementById('ui-bot').style.pointerEvents='none';"

if old in c:
    c = c.replace(old, new)
    print("OK ui-bot oculto en fin")
else:
    print("WARN no encontrado")

# Mostrar ui-bot solo tras iniciarJota con delay
old2 = "document.getElementById('amb-ind').classList.add('show');"
new2 = "document.getElementById('amb-ind').classList.add('show');\n  setTimeout(()=>{document.getElementById('ui-bot').classList.add('show');},3000);"

if old2 in c:
    c = c.replace(old2, new2)
    print("OK ui-bot aparece 3s despues de arrancar")
else:
    print("WARN amb-ind no encontrado")

open('index.html', 'w', encoding='utf-8').write(c)
print("Guardado")