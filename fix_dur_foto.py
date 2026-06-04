with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('dur_foto: 3,', 'dur_foto: 4,')
print('OK' if 'dur_foto: 4,' in c else 'WARN')
open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')