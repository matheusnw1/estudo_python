
filmes_joao = ["Inception", "Matrix", "Interstellar", "Parasite", "Matrix", "Inception"]
filmes_maria = ["Parasite", "Joker", "Interstellar", "1917", "Joker"]

def remover_duplicatas(filmes):
    return set(filmes)

def filmes_em_comum(set1, set2):
    return set1 & set2

def exclusivos(set1, set2): 
    return set1 - set2 

def exibir_relatorio(nome1, filmes1, nome2, filmes2):

    set_joao = remover_duplicatas(filmes1)
    set_maria = remover_duplicatas(filmes2)
    em_comum = filmes_em_comum(set_joao, set_maria)
    exclusivo = exclusivos(set_joao, set_maria)
    exclusivo2 = exclusivos(set_maria, set_joao)

    print(f"{'='*30}")
    print(f"{'RELATÓRIO':^30}")
    print(f"Filmes de {nome1}: {filmes1}")
    print(f"Filmes de {nome2}: {filmes2}")
    print(f'Filmes em comum: {em_comum}')
    print(f'Filmes exclusivos {nome1}: {exclusivo}')
    print(f'Filmes exclusivos {nome2}: {exclusivo2}')

exibir_relatorio('Joao', filmes_joao, 'Maria', filmes_maria)
    
