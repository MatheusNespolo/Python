palavras = (
    "nebula", 
    "dragao", 
    "codigo", 
    "galaxia", 
    "controle", 
    "astro", 
    "energia", 
    "missao", 
    "aventura", 
    "planeta"
)
for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')
            