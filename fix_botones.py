c = open('index.html', 'r', encoding='utf-8').read()
# Ocultar botones durante la portada, solo mostrar en pantalla final
c = c.replace(
    "  // Mostrar botones\n  document.getElementById('ui-bottom').classList.add('show');",
    "  // Botones solo en pantalla final - no mostrar durante portada"
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')