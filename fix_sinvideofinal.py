import re
c = open('index.html', 'r', encoding='utf-8').read()
c = re.sub(
    r'reproducirVideoFinal\(.*?\}\);',
    "document.getElementById('pant-final').classList.add('show');",
    c, flags=re.DOTALL
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')