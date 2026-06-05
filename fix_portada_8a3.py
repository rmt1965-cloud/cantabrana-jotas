with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('},8000);', '},3500);', 1)
print('OK portada 3.5s')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')