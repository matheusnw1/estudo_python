
valor = 286

notas = [100, 50, 20, 10, 5, 1]
resultado = {}

resto = valor

for nota in notas:
    quantidade = resto // nota
    resultado[nota] = quantidade
    resto = resto % nota

print("Valor:", valor)
print("Notas utilizadas:")

for nota, qtd in resultado.items():
    if qtd > 0:
        print(f"{qtd} nota(s) de {nota}")
      
