
numeros = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_atual = numeros[0]
max_global = numeros[0]

inicio = fim = temp_inicio = 0

for i in range(1, len(numeros)):
    if numeros[i] > max_atual + numeros[i]:
        max_atual = numeros[i]
        temp_inicio = i
    else:
        max_atual += numeros[i]

    if max_atual > max_global:
        max_global = max_atual
        inicio = temp_inicio
        fim = i

print("Maior soma:", max_global)
print("Subarray:", numeros[inicio:fim+1])
