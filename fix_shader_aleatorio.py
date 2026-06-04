import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'// SHADER FONDO.*?\(function\(\)\{.*?\}\)\(\);', c, re.DOTALL)
if not m:
    print('ERR: bloque shader no encontrado')
    exit()

nuevo = """// SHADER FONDO — aleatorio entre bruma y seda lite
// ================================================================
(function(){
  const cv=document.getElementById('bg');
  const gl=cv.getContext('webgl');
  if(!gl)return;
  function rsz(){cv.width=window.innerWidth;cv.height=window.innerHeight;gl.viewport(0,0,cv.width,cv.height);}
  window.addEventListener('resize',rsz);rsz();
  const vs='attribute vec2 p;void main(){gl_Position=vec4(p,0,1);}';

  // Elegir shader aleatoriamente
  const useSeda=Math.random()<0.5;

  const fsBruma='precision mediump float;uniform float t;uniform vec2 r;float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5);}float n(vec2 p){vec2 i=floor(p),f=fract(p),u=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),u.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),u.x),u.y);}float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<4;i++){v+=a*n(p);p*=2.1;a*=.5;}return v;}void main(){vec2 uv=gl_FragCoord.xy/r;float f=fbm(uv*2.8+t*.12);float f2=fbm(uv*5.5-t*.08);float cycle=mod(t*.025,1.0);vec3 c1=mix(vec3(.55,.02,.12),vec3(.36,.02,.32),smoothstep(0.,.5,cycle));vec3 c2=mix(vec3(.36,.02,.32),vec3(.16,.03,.42),smoothstep(.5,1.,cycle));vec3 col=mix(c1,mix(c2,c1*1.2,f2),f);col*=(.5+.5*fbm(uv*9.+t*.15));gl_FragColor=vec4(col,1.);}';

  const fsSeda=`precision highp float;
uniform float t;uniform vec2 r;
float h(vec2 p){p=fract(p*vec2(127.1,311.7));p+=dot(p,p+45.3);return fract(p.x*p.y);}
float sn(vec2 p){vec2 i=floor(p),f=fract(p),u=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),u.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),u.x),u.y);}
float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<5;i++){v+=a*sn(p);p=p*2.02+vec2(1.9,4.3);a*=.5;}return v;}
float silk(vec2 p,float s){float ts=t*s;vec2 q=vec2(fbm(p+vec2(ts*.3,ts*.15)),fbm(p+vec2(ts*.15,ts*.3)+vec2(4.2,1.8)));vec2 q2=vec2(fbm(p+2.*q+vec2(ts*.15,ts*.08)+vec2(1.4,7.2)),fbm(p+2.*q+vec2(ts*.08,ts*.15)+vec2(6.8,2.4)));return fbm(p+1.5*q2+vec2(ts*.03,ts*.02));}
vec3 silkPal(float tt){float c=mod(tt*.018,1.);float s=floor(c*6.);float b=smoothstep(.1,.9,fract(c*6.));vec3 cols[7];cols[0]=vec3(.52,.02,.11);cols[1]=vec3(.45,.08,.32);cols[2]=vec3(.12,.04,.48);cols[3]=vec3(.02,.06,.45);cols[4]=vec3(.02,.25,.38);cols[5]=vec3(.02,.32,.18);cols[6]=vec3(.52,.02,.11);int i=int(s);vec3 c1,c2;if(i==0){c1=cols[0];c2=cols[1];}else if(i==1){c1=cols[1];c2=cols[2];}else if(i==2){c1=cols[2];c2=cols[3];}else if(i==3){c1=cols[3];c2=cols[4];}else if(i==4){c1=cols[4];c2=cols[5];}else{c1=cols[5];c2=cols[6];}return mix(c1,c2,b);}
void main(){
  vec2 uv=gl_FragCoord.xy/r;uv.y=1.-uv.y;vec2 p=(uv-.5)*2.8;p.x*=r.x/r.y;
  float f1=silk(p,.06),f2=silk(p*1.5+vec2(2.8,1.4),.05),f3=silk(p*.7+vec2(1.1,3.8),.04),f4=silk(p*3.+vec2(4.8,.7),.09);
  float hgt=pow(smoothstep(.05,.95,f1*.42+f2*.28+f3*.18+f4*.12),.78);
  float e=0.005;
  vec3 N=normalize(vec3((silk(p-vec2(e,0.),.06)-silk(p+vec2(e,0.),.06))*18.,2.*e*12.,(silk(p-vec2(0.,e),.06)-silk(p+vec2(0.,e),.06))*18.));
  vec3 L1=normalize(vec3(sin(t*.06)*.4,1.4,cos(t*.05)*.3)),V=normalize(vec3(0.,1.,.2));
  float d1=max(0.,dot(N,L1));
  float ang=atan(N.x,N.z);vec3 T=normalize(vec3(cos(ang),0.,sin(ang)));
  float asp=pow(max(0.,1.-abs(dot(T,normalize(L1+V)))),28.)*d1;
  float sp2=pow(max(0.,dot(reflect(-L1,N),V)),60.)*d1*.4;
  float fres=pow(1.-clamp(N.y,0.,1.),1.8);
  vec3 b=silkPal(t),b2=silkPal(t+3.5);
  vec3 col=b*.06;
  col=mix(col,b*.45,smoothstep(.06,.30,hgt));col=mix(col,b*.80,smoothstep(.26,.55,hgt));
  col=mix(col,b*1.1,smoothstep(.50,.76,hgt)*pow(d1,.7));
  col=mix(col,mix(b*1.4,vec3(.90,.86,.82),fres*.5),smoothstep(.72,.96,hgt)*pow(d1,.9));
  col*=.12+d1*.90;col+=asp*1.1*vec3(.95,.91,.87)+sp2*.4*vec3(.92,.88,.84);
  col=mix(col,col+b2*.2,smoothstep(.35,.75,hgt)*fres*.4);
  col=mix(col,col*.04,pow(1.-smoothstep(.0,.35,hgt),2.2)*.7);
  col*=.28+.72*(1.-smoothstep(.0,1.1,length(uv-.5)*2.0));
  col=pow(clamp(col/(col+vec3(.55))*1.5,0.,1.),vec3(.86,.87,.88));
  gl_FragColor=vec4(col,1.);}`;

  const fs=useSeda?fsSeda:fsBruma;
  function mk(tp,src){const s=gl.createShader(tp);gl.shaderSource(s,src);gl.compileShader(s);if(!gl.getShaderParameter(s,gl.COMPILE_STATUS)){console.error(gl.getShaderInfoLog(s));return null;}return s;}
  const prog=gl.createProgram();
  const sv=mk(gl.VERTEX_SHADER,vs),sf=mk(gl.FRAGMENT_SHADER,fs);
  if(!sv||!sf){console.warn('Shader fallido, usando bruma');return;}
  gl.attachShader(prog,sv);gl.attachShader(prog,sf);gl.linkProgram(prog);
  if(!gl.getProgramParameter(prog,gl.LINK_STATUS)){console.error(gl.getProgramInfoLog(prog));return;}
  gl.useProgram(prog);
  const buf=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buf);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
  const ap=gl.getAttribLocation(prog,'p');gl.enableVertexAttribArray(ap);gl.vertexAttribPointer(ap,2,gl.FLOAT,false,0,0);
  const ut=gl.getUniformLocation(prog,'t'),ur=gl.getUniformLocation(prog,'r');
  const t0=performance.now();
  (function loop(){rsz();const tt=(performance.now()-t0)/1000;gl.uniform1f(ut,tt);gl.uniform2f(ur,cv.width,cv.height);gl.drawArrays(gl.TRIANGLE_STRIP,0,4);requestAnimationFrame(loop);})();
})();"""

c = c[:m.start()] + nuevo + c[m.end():]
print('OK shader aleatorio aplicado')
open('index.html','w',encoding='utf-8').write(c)
print('Guardado')