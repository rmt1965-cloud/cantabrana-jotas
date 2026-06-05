with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('setTimeout(iniciarJota,6000);', 'setTimeout(iniciarJota,10000);')
print('OK pergamino 10s' if '10000' in c else 'WARN')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')