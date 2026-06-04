with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Cuando se muestra la portada al final, limitar su tamaño
old = "setTimeout(()=>{fi.src=CFG.portada;bl.style.backgroundImage=\"url('\"+CFG.portada+\"')\";fi.onload=()=>{tr.classList.remove('on');fi.classList.add('show');};},"
new = "setTimeout(()=>{fi.src=CFG.portada;bl.style.backgroundImage=\"url('\"+CFG.portada+\"')\";fi.style.maxWidth='75%';fi.style.maxHeight='65vh';fi.onload=()=>{tr.classList.remove('on');fi.classList.add('show');};},"

if old in c:
    c = c.replace(old, new)
    print('OK portada limitada')
else:
    print('WARN no encontrado')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')