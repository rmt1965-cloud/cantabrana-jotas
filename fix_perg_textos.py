with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix encoding roto
fixes = {
    'Ã©': 'é', 'Ã¡': 'á', 'Ã³': 'ó', 'Ãº': 'ú', 'Ã­': 'í',
    'Ã‰': 'É', 'Ã': 'Á', 'Ã"': 'Ó', 'Ãš': 'Ú', 'Ã': 'Í',
    'Ã±': 'ñ', 'Ã': 'Ñ', 'â€™': "'", 'Â·': '·',
}
for mal, bien in fixes.items():
    c = c.replace(mal, bien)
print('OK encoding corregido')

# Sustituir "jotas" por "Jotas y canciones populares"
c = c.replace(
    'Son jotas de otro tiempo.',
    'Son Jotas y canciones populares de otro tiempo.'
)
c = c.replace(
    'Estas jotas son de otro tiempo.',
    'Estas Jotas y canciones populares de otro tiempo.'
)
c = c.replace(
    'Estas canciones<br>son de otra &eacute;poca,<br>algunas pueden herir<br>su sensibilidad',
    'Jotas y canciones populares<br>de otra &eacute;poca,<br>algunas pueden herir<br>su sensibilidad'
)
print('OK textos pergamino actualizados')

# Tamaño fuente mas pequeno para que quepa
c = c.replace(
    "font-size:clamp(20px,6.5vw,30px);font-w",
    "font-size:clamp(14px,4.5vw,20px);font-w"
)
print('OK fuente p-aviso ajustada')

open('index.html', 'w', encoding='utf-8').write(c)
print('Guardado')