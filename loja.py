
vendas = {
    "loja_a": ["notebook", "mouse", "teclado", "notebook", "monitor", "mouse"],
    "loja_b": ["mouse", "headset", "monitor", "headset", "webcam"],
    "loja_c": ["teclado", "notebook", "webcam", "teclado", "headset"]
}

def produtos_unicos(loja):
    return set(vendas[loja])

def produtos_em_todas_lojas(vendas):
    sets = [set(produtos) for produtos in vendas.values()]
    return sets[0].intersection(*sets[1:])

def produtos_exclusivos(loja):
    minha_loja = set(vendas[loja])
    outras_lojas = set()
    for nome, produtos in vendas.items():
        if nome != loja:
            outras_lojas.update(produtos)
    return minha_loja - outras_lojas

def loja_com_mais_variedade(vendas):
    return max(vendas, key=lambda loja: len(set(vendas[loja])))

def todas_as_marcas(vendas):
    resultado = set()
    for produtos in vendas.values():
        resultado.update(produtos)
    return resultado

print("Produtos únicos por loja")
for loja in vendas:
    print(f"{loja}: {produtos_unicos(loja)}")

print("Produtos vendidos em TODAS as lojas")
print(produtos_em_todas_lojas(vendas))

print("Produtos EXCLUSIVOS por loja")
for loja in vendas:
    print(f"{loja}: {produtos_exclusivos(loja)}")

print("Loja com mais variedade")
print(loja_com_mais_variedade(vendas))

print("Catalogo completo")
print(todas_as_marcas(vendas))
