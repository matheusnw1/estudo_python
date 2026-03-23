
perguntas = [

    {

        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '6'],
        'Resposta': '4'
    },
    {   
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '20', '15', '10'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10 / 2   ?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5'
    },
]

acertos = 0
for dados in perguntas:
    print(dados['Pergunta'])
    opcoes = dados['Opções']
    for i, opcao in enumerate(opcoes):
        print(i, opcao, sep= ') ')
    escolha = int(input('Escolha uma opção: '))
    if escolha == opcoes.index(dados['Resposta']):
        acertos += 1
        print('Acertou!')
    else:
        print('Errou')

print(f'Você acertou {acertos} de {len(perguntas)}!')
