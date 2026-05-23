
import string

alfabeto = string.ascii_lowercase
deslocamento = 3

texto = input("Digite uma mensagem: ").lower()

resultado = ""

for letra in texto:

    if letra in alfabeto:

        posicao = alfabeto.index(letra)
        nova_posicao = (posicao + deslocamento) % 26

        resultado += alfabeto[nova_posicao]

    else:
        resultado += letra

print(f"Texto criptografado: {resultado}")
