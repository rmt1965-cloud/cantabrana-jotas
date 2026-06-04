with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

old = """// SHADER FONDO
(function(){
  const cv=document.getElementById('bg');
  const gl=cv.getContext('webgl');
  if(!gl)return;
  function r(){cv.width=window.innerWidth;cv.height=window.innerHeight;gl.viewport(0,0,cv.width,cv.height);}
  window.addEventListener('resize',r);r();
  const vs='attribute vec2 p;void main(){gl_Position=vec4(p,0,1);}';
  const fs='precision mediump float;uniform float t;uniform vec2 r;float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5);}float n(vec2 p){vec2 i=floor(p),f=fract(p),u=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),u.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),u.x),u.y);}float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<4;i++){v+=a*n(p);p*=2.1;a*=.5;}return v;}void main(){vec2 uv=gl_FragCoord.xy/r;float f=fbm(uv*2.8+t*.12);float f2=fbm(uv*5.5-t*.08);vec3 c1=vec3(.05,.03,.01),c2=vec3(.14,.08,.02),c3=vec3(.06,.04,.01);vec3 col=mix(c1,mix(c2,c3,f2),f);col*=(.7+.3*fbm(uv*9.+t*.15));gl_FragColor=vec4(col,1.);}';
  function mk(type,src){const s=gl.createShader(type);gl.shaderSource(s,src);gl.compileShader(s);return s;}
  const prog=gl.createProgram();gl.attachShader(prog,mk(gl.VERTEX_SHADER,vs));gl.attachShader(prog,mk(gl.FRAGMENT_SHADER,fs));gl.linkProgram(prog);gl.useProgram(prog);
  const buf=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buf);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
  const ap=gl.getAttribLocation(prog,'p');gl.enableVertexAttribArray(ap);gl.vertexAttribPointer(ap,2,gl.FLOAT,false,0,0);
  const ut=gl.getUniformLocation(prog,'t'),ur=gl.getUniformLocation(prog,'r');
  const t0=performance.now();
  (function loop(){const t=(performance.now()-t0)/1000;gl.uniform1f(ut,t);gl.uniform2f(ur,cv.width,cv.height);gl.drawArrays(gl.TRIANGLE_STRIP,0,4);requestAnimationFrame(loop);})();
})();"""

new = """// SHADER SEDA — Cantabrana v22
(function(){
  const cv=document.getElementById('bg');
  const gl=cv.getContext('webgl');
  if(!gl)return;
  function rsz(){cv.width=window.innerWidth;cv.height=window.innerHeight;gl.viewport(0,0,cv.width,cv.height);}
  window.addEventListener('resize',rsz);rsz();
  const vs='attribute vec2 p;void main(){gl_Position=vec4(p,0,1);}';
  const fs=`precision highp float;
uniform float t;uniform vec2 r;
float h(vec2 p){p=fract(p*vec2(127.1,311.7));p+=dot(p,p+45.3);return fract(p.x*p.y);}
float sn(vec2 p){vec2 i=floor(p),f=fract(p),u=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),u.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),u.x),u.y);}
float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<7;i++){v+=a*sn(p);p=p*2.02+vec2(1.9,4.3);a*=.5;}return v;}
float silk(vec2 p,float s){float ts=t*s;vec2 q=vec2(fbm(p+vec2(ts*.3,ts*.15)),fbm(p+vec2(ts*.15,ts*.3)+vec2(4.2,1.8)));vec2 q2=vec2(fbm(p+2.5*q+vec2(ts*.2,ts*.1)+vec2(1.4,7.2)),fbm(p+2.5*q+vec2(ts*.1,ts*.2)+vec2(6.8,2.4)));vec2 q3=vec2(fbm(p+2.*q2+vec2(ts*.1,ts*.05)+vec2(3.1,4.8)),fbm(p+2.*q2+vec2(ts*.05,ts*.1)+vec2(0.8,9.2)));return fbm(p+1.8*q3+vec2(ts*.04,ts*.02));}
vec3 calcN(vec2 p){float e=0.004;return normalize(vec3((silk(p-vec2(e,0.),.06)-silk(p+vec2(e,0.),.06))*20.,2.*e*12.,(silk(p-vec2(0.,e),.06)-silk(p+vec2(0.,e),.06))*20.));}
vec3 silkPalette(float tt){float cycle=mod(tt*.018,1.);float seg=floor(cycle*6.);float bl=smoothstep(.1,.9,fract(cycle*6.));vec3 cols[7];cols[0]=vec3(.52,.02,.11);cols[1]=vec3(.45,.08,.32);cols[2]=vec3(.12,.04,.48);cols[3]=vec3(.02,.06,.45);cols[4]=vec3(.02,.25,.38);cols[5]=vec3(.02,.32,.18);cols[6]=vec3(.52,.02,.11);int i=int(seg);vec3 c1,c2;if(i==0){c1=cols[0];c2=cols[1];}else if(i==1){c1=cols[1];c2=cols[2];}else if(i==2){c1=cols[2];c2=cols[3];}else if(i==3){c1=cols[3];c2=cols[4];}else if(i==4){c1=cols[4];c2=cols[5];}else{c1=cols[5];c2=cols[6];}return mix(c1,c2,bl);}
void main(){
  vec2 uv=gl_FragCoord.xy/r;uv.y=1.-uv.y;vec2 p=(uv-.5)*2.8;p.x*=r.x/r.y;
  float f1=silk(p,.06),f2=silk(p*1.5+vec2(2.8,1.4),.05),f3=silk(p*.7+vec2(1.1,3.8),.04),f4=silk(p*3.+vec2(4.8,.7),.10),f5=silk(p*6.+vec2(2.1,5.3),.16);
  float hgt=pow(smoothstep(.05,.95,f1*.38+f2*.26+f3*.20+f4*.10+f5*.06),.78);
  vec3 N=calcN(p);float NdY=clamp(N.y,0.,1.);
  vec3 L1=normalize(vec3(sin(t*.06)*.4,1.4,cos(t*.05)*.3)),L2=normalize(vec3(-.4,.8,.5)),V=normalize(vec3(0.,1.,.2));
  float d1=max(0.,dot(N,L1)),d2=max(0.,dot(N,L2))*.4,diff=d1+d2;
  float ang=atan(N.x,N.z);vec3 T=normalize(vec3(cos(ang),0.,sin(ang)));
  float anisoSpec=pow(max(0.,1.-abs(dot(T,normalize(L1+V)))),32.)*d1;
  float spec2=pow(max(0.,dot(reflect(-L1,N),V)),80.)*d1*.5;
  float fres=pow(1.-NdY,1.8);
  vec3 b=silkPalette(t),b2=silkPalette(t+3.5);
  vec3 col=b*.06;
  col=mix(col,b*.45,smoothstep(.06,.30,hgt));col=mix(col,b*.75,smoothstep(.26,.52,hgt));
  col=mix(col,b*1.1+vec3(.06,.04,.03),smoothstep(.48,.74,hgt)*pow(diff,.7));
  col=mix(col,mix(b*1.5,vec3(.92,.88,.84),fres*.5),smoothstep(.70,.94,hgt)*pow(d1,.9));
  col*=.10+diff*.90;
  col+=anisoSpec*1.2*mix(vec3(.96,.92,.88),b*2.,fres*.4)+spec2*.5*vec3(.94,.90,.86);
  col+=fres*.2*mix(vec3(.90,.86,.80),b*1.4,.4)*diff;
  col+=pow(max(0.,sin(hgt*15.+ang*3.+t*.8)*.5+.5),4.)*.10*mix(b*1.5,vec3(.92,.88,.84),fres*.5)*d1;
  col=mix(col,col+b2*.25,smoothstep(.35,.75,hgt)*fres*.5);
  col=mix(col,col*.04,pow(1.-smoothstep(.0,.35,hgt),2.4)*.75);
  col*=.25+.75*(1.-smoothstep(.0,1.1,length(uv-.5)*2.0));
  col=pow(clamp(col/(col+vec3(.55))*1.5,0.,1.),vec3(.86,.87,.88));
  gl_FragColor=vec4(col,1.);}`;
  function mk(tp,src){const s=gl.createShader(tp);gl.shaderSource(s,src);gl.compileShader(s);if(!gl.getShaderParameter(s,gl.COMPILE_STATUS))console.error(gl.getShaderInfoLog(s));return s;}
  const prog=gl.createProgram();gl.attachShader(prog,mk(gl.VERTEX_SHADER,vs));gl.attachShader(prog,mk(gl.FRAGMENT_SHADER,fs));gl.linkProgram(prog);gl.useProgram(prog);
  const buf=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buf);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
  const ap=gl.getAttribLocation(prog,'p');gl.enableVertexAttribArray(ap);gl.vertexAttribPointer(ap,2,gl.FLOAT,false,0,0);
  const ut=gl.getUniformLocation(prog,'t'),ur=gl.getUniformLocation(prog,'r');
  const t0=performance.now();
  (function loop(){rsz();const tt=(performance.now()-t0)/1000;gl.uniform1f(ut,tt);gl.uniform2f(ur,cv.width,cv.height);gl.drawArrays(gl.TRIANGLE_STRIP,0,4);requestAnimationFrame(loop);})();

  // Texto pulso y color dinámico
  const claras=[
    {c:'#ffffff',sh:'0 2px 10px rgba(0,0,0,0.95)',b:'rgba(255,255,255,0.08)'},
    {c:'#f0c060',sh:'0 2px 10px rgba(0,0,0,0.95)',b:'rgba(240,192,96,0.10)'},
    {c:'#d0d8e8',sh:'0 2px 10px rgba(0,0,0,0.95)',b:'rgba(208,216,232,0.08)'},
  ];
  let ci=0;
  function aplColor(col){
    const btn=document.getElementById('ld-btn');
    const tit=document.querySelector('.ld-titulo');
    const sub=document.querySelector('.ld-subtitulo');
    const aut=document.querySelector('.ld-autor');
    if(btn){btn.style.color=col.c;btn.style.borderColor=col.c;btn.style.background=col.b;}
    if(tit)tit.style.color=col.c;
    if(sub)sub.style.color=col.c;
    if(aut)aut.style.color=col.c;
  }
  aplColor(claras[0]);
  setInterval(()=>{ci=Math.floor(Date.now()/4000)%claras.length;aplColor(claras[ci]);},400);
})();"""

if '// SHADER FONDO' in c:
    c = c.replace(old, new)
    if new[:30] in c:
        print('OK shader seda aplicado')
    else:
        # Buscar y reemplazar más flexible
        import re
        c2 = open('index.html','r',encoding='utf-8').read()
        m = re.search(r'// SHADER FONDO\s*\(function\(\)\{.*?\}\)\(\);', c2, re.DOTALL)
        if m:
            c = c2[:m.start()] + new + c2[m.end():]
            print('OK shader seda (variante regex)')
        else:
            print('ERR: no encontrado')
else:
    print('ERR: marca // SHADER FONDO no encontrada')

# Añadir CSS pulso al botón de inicio
css_pulso = """
/* PULSO BOTON INICIO */
@keyframes pulso-btn{0%,100%{opacity:.45;transform:scale(1);}50%{opacity:1;transform:scale(1.04);}}
@keyframes pulso-glow{0%,100%{box-shadow:0 0 0 0 currentColor;}50%{box-shadow:0 0 14px 4px currentColor;}}
#ld-btn{animation:pulso-btn 2.4s ease-in-out infinite,pulso-glow 2.4s ease-in-out infinite;}"""

if 'pulso-btn' not in c:
    c = c.replace('</style>', css_pulso + '\n</style>')
    print('OK CSS pulso añadido')

open('index.html','w',encoding='utf-8').write(c)
print('Guardado OK')