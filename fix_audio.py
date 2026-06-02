c = open('index.html', 'r', encoding='utf-8').read()
c = c.replace(
    "  jotas_url: 'https://github.com/rmt1965-cloud/cantabrana-v22/releases/download/V2.0/',",
    "  jotas_url: 'audio/',"
)
open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')