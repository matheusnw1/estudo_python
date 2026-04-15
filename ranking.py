
jogadores = [
    {"nome": "Ana", "pontos": 150},
    {"nome": "Carlos", "pontos": 300},
    {"nome": "Beatriz", "pontos": 250},
    {"nome": "Daniel", "pontos": 100},
    {"nome": "Eduardo", "pontos": 200}
]

print("Jogadores:")
for j in jogadores:
    print(f"{j['nome']} - {j['pontos']} pontos")

ordenados = sorted(jogadores, key=lambda x: x["pontos"], reverse=True)

top3 = ordenados[:3]

soma = 0
for j in jogadores:
    soma += j["pontos"]

media = soma / len(jogadores)

acima_media = []

for j in jogadores:
    if j["pontos"] > media:
        acima_media.append(j["nome"])

print("\nRanking:")
for j in ordenados:
    print(f"{j['nome']} - {j['pontos']}")

print("\nTop 3:")
for j in top3:
    print(j["nome"])

print(f"\nMédia de pontos: {media}")

print("Jogadores acima da média:", acima_media)
