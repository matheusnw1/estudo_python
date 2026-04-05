
usuarios = {
    "ana": {"senha": "1234", "tentativas": 0, "bloqueado": False},
    "carlos": {"senha": "abcd", "tentativas": 0, "bloqueado": False},
    "bia": {"senha": "senha123", "tentativas": 0, "bloqueado": False}
}

tentativas_login = [
    {"usuario": "ana", "senha": "1111"},
    {"usuario": "ana", "senha": "2222"},
    {"usuario": "ana", "senha": "1234"},
    {"usuario": "carlos", "senha": "errado"},
    {"usuario": "carlos", "senha": "abcd"},
    {"usuario": "bia", "senha": "x"},
    {"usuario": "bia", "senha": "y"},
    {"usuario": "bia", "senha": "z"}
]

print("Usuários:")
for u in usuarios:
    print(u)

for tentativa in tentativas_login:
    user = tentativa["usuario"]
    senha = tentativa["senha"]

    if user in usuarios:
        if usuarios[user]["bloqueado"]:
            continue

        if senha == usuarios[user]["senha"]:
            usuarios[user]["tentativas"] = 0
        else:
            usuarios[user]["tentativas"] += 1

        if usuarios[user]["tentativas"] >= 3:
            usuarios[user]["bloqueado"] = True

bloqueados = []

for user, dados in usuarios.items():
    if dados["bloqueado"]:
        bloqueados.append(user)

print("\nStatus final:")
for user, dados in usuarios.items():
    print(user, dados)

print("\nUsuários bloqueados:", bloqueados)
