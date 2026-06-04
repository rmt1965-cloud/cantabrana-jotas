with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

old = "function finJota(){\n  if(jotaFin)return;jotaFin=true;\n  const ub=document.getElementById('ui-bot');ub.style.opacity='0';ub.style.pointerEvents='none';"
new = "function finJota(){\n  if(jotaFin)return;jotaFin=true;\n  const ub=document.getElementById('ui-bot');ub.style.opacity='0';ub.style.pointerEvents='none';\n  document.getElementById('ticker').style.display='none';"

if old in c:
    c = c.replace(old, new)
    print('OK ticker oculto al fin')
else:
    # variante sin el ub
    old2 = "function finJota(){\n  if(jotaFin)return;jotaFin=true;"
    new2 = "function finJota(){\n  if(jotaFin)return;jotaFin=true;\n  document.getElementById('ticker').style.display='none';"
    if old2 in c:
        c = c.replace(old2, new2)
        print('OK ticker variante')
    else:
        print('WARN no encontrado')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')