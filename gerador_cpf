import random

def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]

    total = sum(num * peso for num, peso in zip(cpf, range(10, 1, -1)))
    resultado = (total * 10) % 11
    digito1 = resultado if resultado <= 9 else 0

    cpf_com_digito1 = cpf + [digito1]
    total2 = sum(num * peso for num, peso in zip(cpf_com_digito1, range(11, 1, -1)))
    resultado2 = (total2 * 10) % 11
    digito2 = resultado2 if resultado2 <= 9 else 0

    cpf_completo = ''.join(map(str, cpf)) + str(digito1) + str(digito2)
    return cpf_completo

def main():
    for _ in range(5):
        print(f'CPF gerado: {gerar_cpf()}')

if __name__ == "__main__":
    main()
