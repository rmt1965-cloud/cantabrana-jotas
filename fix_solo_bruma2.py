import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'// SHADER FONDO.*?\(function\(\)\{.*?\}\)\(\);', c, re.DOTALL)
if m:
    nuevo = ('// SHADER FONDO\n'
'// ================================================================\n'
'(function(){\n'
'  const cv=document.getElementById(\'bg\');\n'
'  const gl=cv.getContext(\'webgl\');\n'
'  if(!gl)return;\n'
'  function r(){cv.width=window.innerWidth;cv.height=window.innerHeight;gl.viewport(0,0,cv.width,cv.height);}\n'
'  window.addEventListener(\'resize\',r);r();\n'
'  const vs=\'attribute vec2 p;void main(){gl_Position=vec4(p,0,1);}\';\n'
'  const fs=\'precision mediump float;uniform float t;uniform vec2 r;float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5);}float n(vec2 p){vec2 i=floor(p),f=fract(p),u=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),u.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),u.x),u.y);}float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<4;i++){v+=a*n(p);p*=2.1;a*=.5;}return v;}void main(){vec2 uv=gl_FragCoord.xy/r;float f=fbm(uv*2.8+t*.12);float f2=fbm(uv*5.5-t*.08);float cy=mod(t*.025,1.0);vec3 c1=mix(vec3(.55,.02,.12),vec3(.36,.02,.32),smoothstep(0.,.5,cy));vec3 c2=mix(vec3(.36,.02,.32),vec3(.16,.03,.42),smoothstep(.5,1.,cy));vec3 col=mix(c1,mix(c2,c1*1.2,f2),f);col*=(.5+.5*fbm(uv*9.+t*.15));gl_FragColor=vec4(col,1.);}\';\n'
'  function mk(type,src){const s=gl.createShader(type);gl.shaderSource(s,src);gl.compileShader(s);return s;}\n'
'  const prog=gl.createProgram();gl.attachShader(prog,mk(gl.VERTEX_SHADER,vs));gl.attachShader(prog,mk(gl.FRAGMENT_SHADER,fs));gl.linkProgram(prog);gl.useProgram(prog);\n'
'  const buf=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buf);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);\n'
'  const ap=gl.getAttribLocation(prog,\'p\');gl.enableVertexAttribArray(ap);gl.vertexAttribPointer(ap,2,gl.FLOAT,false,0,0);\n'
'  const ut=gl.getUniformLocation(prog,\'t\'),ur=gl.getUniformLocation(prog,\'r\');\n'
'  const t0=performance.now();\n'
'  (function loop(){const t=(performance.now()-t0)/1000;gl.uniform1f(ut,t);gl.uniform2f(ur,cv.width,cv.height);gl.drawArrays(gl.TRIANGLE_STRIP,0,4);requestAnimationFrame(loop);})();\n'
'})();')
    c = c[:m.start()] + nuevo + c[m.end():]
    print('OK bruma magenta aplicada')
else:
    print('ERR no encontrado')

open('index.html','w',encoding='utf-8').write(c)
print('Guardado')