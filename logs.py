
logs = [
    {"usuario": "ana", "acao": "login", "hora": "10:00"},
    {"usuario": "carlos", "acao": "erro", "hora": "10:05"},
    {"usuario": "ana", "acao": "compra", "hora": "10:10"},
    {"usuario": "bia", "acao": "login", "hora": "10:00"},
    {"usuario": "ana", "acao": "erro", "hora": "10:15"},
    {"usuario": "carlos", "acao": "compra", "hora": "10:20"},
    {"usuario": "bia", "acao": "erro", "hora": "10:25"},
    {"usuario": "ana", "acao": "logout", "hora": "10:30"}
]

acoes_contagem = {}
usuarios_contagem = {}
horarios_contagem = {}
usuarios_com_erro = set()
total_erros = 0

for log in logs:
    usuario = log["usuario"]
    acao = log["acao"]
    hora = log["hora"]

    acoes_contagem[acao] = acoes_contagem.get(acao, 0) + 1
    usuarios_contagem[usuario] = usuarios_contagem.get(usuario, 0) + 1
    horarios_contagem[hora] = horarios_contagem.get(hora, 0) + 1

    if acao == "erro":
        total_erros += 1
        usuarios_com_erro.add(usuario)

usuario_mais_ativo = max(usuarios_contagem, key=usuarios_contagem.get)
hora_mais_movimentada = max(horarios_contagem, key=horarios_contagem.get)
total_eventos = len(logs)

print("Ações:", acoes_contagem)
print("Usuário mais ativo:", usuario_mais_ativo)
print("Total de erros:", total_erros)
print("Usuários com erro:", list(usuarios_com_erro))
print("Hora com mais eventos:", hora_mais_movimentada)
print("Total de eventos:", total_eventos)
