
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 5

n = len(pesos)

dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(capacidade + 1):
        if pesos[i - 1] <= w:
            dp[i][w] = max(
                valores[i - 1] + dp[i - 1][w - pesos[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

print("Valor máximo:", dp[n][capacidade])
