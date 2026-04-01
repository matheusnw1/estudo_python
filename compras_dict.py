
produtos = {
    "Notebook": {"preco": 3500, "estoque": 10},
    "Mouse": {"preco": 80, "estoque": 50},
    "Teclado": {"preco": 150, "estoque": 20},
    "Monitor": {"preco": 1200, "estoque": 5}
}

print("Produtos:")
for nome, dados in produtos.items():
    print(f"{nome} - Preço: R${dados['preco']} | Estoque: {dados['estoque']}")

total = 0
for dados in produtos.values():
    total += dados["preco"] * dados["estoque"]

print(f"\nValor total do estoque: R${total}")

mais_caro = None
maior_preco = 0

for nome, dados in produtos.items():
    if dados["preco"] > maior_preco:
        maior_preco = dados["preco"]
        mais_caro = nome

print(f"Produto mais caro: {mais_caro} (R${maior_preco})")

estoque_baixo = {}

for nome, dados in produtos.items():
    if dados["estoque"] < 10:
        estoque_baixo[nome] = dados

print("\nEstoque baixo:", estoque_baixo)

for dados in produtos.values():
    dados["preco"] *= 0.9

print("\nProdutos com desconto:")
for nome, dados in produtos.items():
    print(f"{nome}: R${dados['preco']:.2f}")
  
