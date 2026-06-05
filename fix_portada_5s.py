with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('},3500);', '},5000);', 1)
print('OK portada 5s' if '5000' in c else 'WARN')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')