with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('setTimeout(iniciarJota,2500);', 'setTimeout(iniciarJota,6000);')
print('OK pergamino 6s' if '6000' in c else 'WARN')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')