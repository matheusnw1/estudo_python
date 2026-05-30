
import json
from pathlib import Path

ARQUIVO = "tarefas.json"

if Path(ARQUIVO).exists():
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        tarefas = json.load(f)
else:
    tarefas = []

while True:

    print("""
1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover tarefa
5 - Sair
""")

    opcao = input("Escolha: ")

    if opcao == "1":

        titulo = input("Tarefa: ")

        tarefas.append({
            "titulo": titulo,
            "concluida": False
        })

    elif opcao == "2":

        for i, tarefa in enumerate(tarefas, start=1):

            status = "✓" if tarefa["concluida"] else "✗"

            print(f"{i}. [{status}] {tarefa['titulo']}")

    elif opcao == "3":

        indice = int(input("Número da tarefa: ")) - 1

        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True

    elif opcao == "4":

        indice = int(input("Número da tarefa: ")) - 1

        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)

    elif opcao == "5":

        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(tarefas, f, indent=4, ensure_ascii=False)

        break

    else:
        print("Opção inválida.")
      
