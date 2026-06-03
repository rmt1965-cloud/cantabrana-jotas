c = open('index.html', 'r', encoding='utf-8').read()

# Favicon SVG inline
favicon = """<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='45' fill='%238B1A1A' stroke='%23c8922a' stroke-width='3'/><text y='65' x='50' text-anchor='middle' font-size='50' font-family='serif' fill='%23f0c060'>C</text></svg>">"""

c = c.replace('</title>', '</title>\n' + favicon)

# Aumentar tiempo despedida a 8 segundos
c = c.replace(
    '  }, 5000);',
    '  }, 8000);'
)

# Ken Burns mas lento para la despedida
c = c.replace(
    "img.style.animation = KB_ANIMS[idxKB] + ' 8s ease-in-out forwards';",
    "img.style.animation = KB_ANIMS[idxKB] + ' 12s ease-in-out forwards';"
)

open('index.html', 'w', encoding='utf-8').write(c)
print('Listo')