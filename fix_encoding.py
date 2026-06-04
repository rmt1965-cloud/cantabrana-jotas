# Leer en latin-1 para capturar los caracteres mal codificados
with open('index.html', 'r', encoding='latin-1') as f:
    c = f.read()

# Recodificar correctamente a UTF-8
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

# Verificar que los acentos quedaron bien
if 'Ã' in c:
    print("WARN: aun hay caracteres Ã - el archivo estaba en UTF-8, aplicando fix manual")
    # Fix manual de los caracteres dobles mas comunes
    fixes = {
        'Ã©': 'é', 'Ã¡': 'á', 'Ã³': 'ó', 'Ãº': 'ú', 'Ã­': 'í',
        'Ã‰': 'É', 'Ã': 'Á', 'Ã"': 'Ó', 'Ãš': 'Ú', 'Ã': 'Í',
        'Ã±': 'ñ', 'Ã': 'Ñ', 'Ã¼': 'ü', 'Ã¤': 'ä',
        'â€™': "'", 'â€œ': '"', 'â€': '"', 'â€"': '—',
        'Â·': '·', 'Â¡': '¡', 'Â¿': '¿',
    }
    with open('index.html', 'r', encoding='utf-8') as f:
        c2 = f.read()
    for mal, bien in fixes.items():
        c2 = c2.replace(mal, bien)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c2)
    print('OK encoding corregido manualmente')
else:
    print('OK encoding UTF-8 correcto')