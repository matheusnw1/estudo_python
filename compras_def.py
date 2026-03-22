
produtos = [
    {"nome": "Camiseta", "preco": 49.90, "quantidade": 3},
    {"nome": "Tênis",    "preco": 199.90, "quantidade": 1},
    {"nome": "Meia",     "preco": 12.50, "quantidade": 6},
]

def calcular_total_item(preco, quantidade):
    total =  preco * quantidade
    return total

def aplicar_desconto(total):

   

    if total > 300:
        return total * (1 - 0.10)
    elif total > 100:
        return total * (1 - 0.05) 
    else:
        return 'Sem desconto'

    
def exibir_item(produto): 
    preco = (produto['preco'])
    quantidade = (produto['quantidade'])
    total = calcular_total_item(preco, quantidade)
    print(produto['nome']) 
    print(preco)            
    print(quantidade)      
    print(total)  
    return total


def processecar_carrinho(produtos):
    for dados in produtos:
        total = exibir_item(dados)
        total_com_desconto = aplicar_desconto(total)
        print(total_com_desconto)

processecar_carrinho(produtos)
