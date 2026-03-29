
jogadores = {
    "time_a": ["Carlos", "Ana", "Bruno", "Carlos", "Diego", "Ana"],
    "time_b": ["Bruno", "Elena", "Felipe", "Elena", "Carlos"],
    "time_c": ["Ana", "Gabriel", "Felipe", "Gabriel", "Diego"]
}

def jogadores_unicos(time):
    return set(jogadores[time])

def jogadores_em_todos_times(jogadores):
    sets = [set(elenco) for elenco in jogadores.values()]
    return sets[0].intersection(*sets[1:])

def jogadores_exclusivos(time):
    meu_time = set(jogadores[time])
    outros_times = set()
    for nome, elenco in jogadores.items():
        if nome != time:
            outros_times.update(elenco)
    return meu_time - outros_times

def time_com_mais_jogadores(jogadores):
    return max(jogadores, key=lambda time: len(set(jogadores[time])))

def todos_os_jogadores(jogadores):
    resultado = set()
    for elenco in jogadores.values():
        resultado.update(elenco)
    return resultado

def jogadores_em_dois_times(jogadores):
    todos = list(jogadores.values())
    aparecem_em_dois = set()
    nomes = list(jogadores.keys())
    for i in range(len(nomes)):
        for j in range(i + 1, len(nomes)):
            em_comum = set(todos[i]) & set(todos[j])
            aparecem_em_dois.update(em_comum)
    jogam_em_todos = jogadores_em_todos_times(jogadores)
    return aparecem_em_dois - jogam_em_todos

print("Jogadores unicos por time")
for time in jogadores:
    print(f"{time}: {jogadores_unicos(time)}")

print("Jogadores presentes em TODOS os times")
print(jogadores_em_todos_times(jogadores))

print("Jogadores EXCLUSIVOS por time")
for time in jogadores:
    print(f"{time}: {jogadores_exclusivos(time)}")

print("Time com mais jogadores diferentes")
print(time_com_mais_jogadores(jogadores))

print("Elenco completo")
print(todos_os_jogadores(jogadores))

print("Jogadores em exatamente dois times")
print(jogadores_em_dois_times(jogadores))
