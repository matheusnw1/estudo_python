
senhas = [
    "abc123",
    "senhaSegura1",
    "12345678",
    "abc",
    "minhaSenha2024",
    "python"
]

print("Senhas:")
for s in senhas:
    print(s)

senhas_fortes = []

for s in senhas:
    tem_numero = any(c.isdigit() for c in s)
    if len(s) >= 8 and tem_numero:
        senhas_fortes.append(s)

quantidade_fortes = len(senhas_fortes)

maior_senha = ""
for s in senhas:
    if len(s) > len(maior_senha):
        maior_senha = s

print("\nSenhas fortes:", senhas_fortes)
print("Quantidade de senhas fortes:", quantidade_fortes)
print("Maior senha:", maior_senha)
