
pedidos = [
    {"cliente": "Ana", "item": "Hamburguer", "quantidade": 2, "preco": 25},
    {"cliente": "Carlos", "item": "Pizza", "quantidade": 1, "preco": 40},
    {"cliente": "Ana", "item": "Refrigerante", "quantidade": 3, "preco": 5},
    {"cliente": "Beatriz", "item": "Hamburguer", "quantidade": 1, "preco": 25},
    {"cliente": "Carlos", "item": "Hamburguer", "quantidade": 2, "preco": 25},
    {"cliente": "Daniel", "item": "Pizza", "quantidade": 2, "preco": 40}
]

print("Pedidos:")
for p in pedidos:
    print(f"{p['cliente']} pediu {p['quantidade']}x {p['item']}")

faturamento_total = 0

for p in pedidos:
    faturamento_total += p["quantidade"] * p["preco"]

itens_contagem = {}

for p in pedidos:
    item = p["item"]
    itens_contagem[item] = itens_contagem.get(item, 0) + p["quantidade"]

mais_pedido = max(itens_contagem, key=itens_contagem.get)

gasto_clientes = {}

for p in pedidos:
    cliente = p["cliente"]
    total = p["quantidade"] * p["preco"]
    gasto_clientes[cliente] = gasto_clientes.get(cliente, 0) + total

clientes_acima_100 = []

for cliente, total in gasto_clientes.items():
    if total > 100:
        clientes_acima_100.append(cliente)

print("\nFaturamento total:", faturamento_total)
print("Item mais pedido:", mais_pedido)
print("Gasto por cliente:", gasto_clientes)
print("Clientes que gastaram mais de R$100:", clientes_acima_100)
