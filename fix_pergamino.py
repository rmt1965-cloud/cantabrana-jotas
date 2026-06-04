with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# +1 segundo mas al pergamino (5000 -> 6000)
c = c.replace('setTimeout(iniciarJota,5000);', 'setTimeout(iniciarJota,6000);')
print('OK +1s pergamino' if '6000' in c else 'WARN timeout')

# Deshabilitar pergamino02
c = c.replace("'fotos/pergaminos/pergamino02.jpg',", '')
print('OK pergamino02 deshabilitado' if 'pergamino02' not in c else 'WARN pergamino02')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')