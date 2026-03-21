
pessoas = []

while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ")
    
    if nome.lower() == "sair":
        break
    
    idade = int(input("Digite a idade: "))
    
    pessoa = {
        "nome": nome,
        "idade": idade
    }
    
    pessoas.append(pessoa)

total_pessoas = len(pessoas)

soma_idades = 0
mais_velho = pessoas[0]
menores = []

for p in pessoas:
    soma_idades += p["idade"]
    
    if p["idade"] > mais_velho["idade"]:
        mais_velho = p
    
    if p["idade"] < 18:
        menores.append(p["nome"])

media_idade = soma_idades / total_pessoas

print("\n--- RESULTADOS ---")
print(f"Total de pessoas: {total_pessoas}")
print(f"Média de idade: {media_idade:.2f}")
print(f"Pessoa mais velha: {mais_velho['nome']}")
print("Menores de idade:", menores)
