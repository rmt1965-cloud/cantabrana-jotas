import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

orig = c

# FIX 1: pergamino 2 segundos mas
c = c.replace('resolve();},1200)', 'resolve();},3200)')
print('FIX1:', 'OK' if c != orig else 'NO ENCONTRADO')

# FIX 2: aleatoriedad real fotos intro
m = re.search(r'[ \t]*const fotos_intro=shuffle\(CFG\.fotos_intro\);', c)
if m:
    ind = re.match(r'([ \t]*)', m.group()).group(1)
    rep = (ind + 'let histI=[];try{histI=JSON.parse(localStorage.getItem("cant_intro")||"[]");}catch(e){}\n' +
           ind + 'let noVistasI=CFG.fotos_intro.filter(f=>!histI.includes(f));\n' +
           ind + 'if(noVistasI.length<3){histI=[];noVistasI=CFG.fotos_intro;}\n' +
           ind + 'const fotos_intro=shuffle(noVistasI);\n' +
           ind + 'const nvi=[...histI,...fotos_intro.slice(0,3)].slice(-Math.max(3,Math.floor(CFG.fotos_intro.length*0.6)));\n' +
           ind + 'try{localStorage.setItem("cant_intro",JSON.stringify(nvi));}catch(e){}')
    c = c[:m.start()] + rep + c[m.end():]
    print('FIX2: OK')
else:
    print('FIX2: NO ENCONTRADO')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')