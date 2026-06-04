with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fade out ventanas: 3200ms -> 1500ms
c = c.replace(
    'setTimeout(()=>{div.style.display=\'none\';div.style.opacity=\'1\';resolve();},3200);',
    'setTimeout(()=>{div.style.display=\'none\';div.style.opacity=\'1\';resolve();},1500);'
)
print('OK fade out ventanas 1500ms' if '1500' in c else 'WARN')

# Timeout pergamino: 5000ms -> 2500ms
c = c.replace('setTimeout(iniciarJota,5000);', 'setTimeout(iniciarJota,2500);')
print('OK pergamino 2500ms' if '2500' in c else 'WARN')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')