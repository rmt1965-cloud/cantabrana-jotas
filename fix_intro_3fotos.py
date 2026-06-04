with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

old = """    let histI=[];try{histI=JSON.parse(localStorage.getItem("cant_intro")||"[]");}catch(e){}
    let noVistasI=CFG.fotos_intro.filter(f=>!histI.includes(f));
    if(noVistasI.length<3){histI=[];noVistasI=CFG.fotos_intro;}
    const fotos_intro=shuffle(noVistasI);
    const nvi=[...histI,...fotos_intro.slice(0,3)].slice(-Math.max(3,Math.floor(CFG.fotos_intro.length*0.6)));
    try{localStorage.setItem("cant_intro",JSON.stringify(nvi));}catch(e){}
    const ventanas=[
      {src:fotos_intro[0], leyenda:grupo[0]},
      {src:fotos_intro[1], leyenda:grupo[1]},
      {src:fotos_intro[2], leyenda:grupo[2]},
    ];"""

new = """    let histI=[];try{histI=JSON.parse(localStorage.getItem("cant_intro")||"[]");}catch(e){}
    let noVistasI=CFG.fotos_intro.filter(f=>!histI.includes(f));
    if(noVistasI.length<3){histI=[];noVistasI=[...CFG.fotos_intro];}
    const fotos_intro=shuffle(noVistasI);
    // Garantizar siempre 3 fotos distintas
    const pool3=fotos_intro.slice(0,3);
    while(pool3.length<3){
      const extra=CFG.fotos_intro.find(f=>!pool3.includes(f));
      if(extra)pool3.push(extra);else break;
    }
    const nvi=[...histI,...pool3].slice(-Math.max(3,Math.floor(CFG.fotos_intro.length*0.6)));
    try{localStorage.setItem("cant_intro",JSON.stringify(nvi));}catch(e){}
    const ventanas=[
      {src:pool3[0], leyenda:grupo[0]},
      {src:pool3[1], leyenda:grupo[1]},
      {src:pool3[2], leyenda:grupo[2]},
    ];"""

if old in c:
    c = c.replace(old, new)
    print('OK siempre 3 fotos distintas')
else:
    print('WARN no encontrado exacto')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')