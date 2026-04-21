
pedidos = [
    {
        "cliente": "Ana",
        "itens": [
            {"produto": "Notebook", "quantidade": 1, "preco": 3500},
            {"produto": "Mouse", "quantidade": 2, "preco": 80}
        ]
    },
    {
        "cliente": "Carlos",
        "itens": [
            {"produto": "Teclado", "quantidade": 1, "preco": 150},
            {"produto": "Monitor", "quantidade": 2, "preco": 1200}
        ]
    },
    {
        "cliente": "Ana",
        "itens": [
            {"produto": "Mouse", "quantidade": 1, "preco": 80},
            {"produto": "Teclado", "quantidade": 1, "preco": 150}
        ]
    },
    {
        "cliente": "Beatriz",
        "itens": [
            {"produto": "Notebook", "quantidade": 1, "preco": 3500}
        ]
    }
]

faturamento_total = 0
gasto_clientes = {}
produtos_vendidos = {}
pedidos_caros = []

for pedido in pedidos:
    cliente = pedido["cliente"]
    total_pedido = 0

    for item in pedido["itens"]:
        subtotal = item["quantidade"] * item["preco"]
        total_pedido += subtotal

        produto = item["produto"]
        produtos_vendidos[produto] = produtos_vendidos.get(produto, 0) + item["quantidade"]

    faturamento_total += total_pedido

    gasto_clientes[cliente] = gasto_clientes.get(cliente, 0) + total_pedido

    if total_pedido > 500:
        pedidos_caros.append({"cliente": cliente, "total": total_pedido})

cliente_top = max(gasto_clientes, key=gasto_clientes.get)

produto_top = max(produtos_vendidos, key=produtos_vendidos.get)

ranking = sorted(gasto_clientes.items(), key=lambda x: x[1], reverse=True)

print("Faturamento total:", faturamento_total)
print("Cliente que mais gastou:", cliente_top)
print("Produto mais vendido:", produto_top)

print("\nRanking de clientes:")
for nome, valor in ranking:
    print(f"{nome}: R${valor}")

print("\nPedidos acima de R$500:")
for p in pedidos_caros:
    print(p)
  
