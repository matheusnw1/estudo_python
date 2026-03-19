import os
import shutil

tipos = {
    "Imagens": [".png", ".jpg", ".jpeg"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Musicas": [".mp3", ".wav"]
}

pasta = input("Digite o caminho da pasta que deseja organizar: ")
contador = 0

for arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho_arquivo):

        for pasta_destino, extensoes in tipos.items():

            if any(arquivo.lower().endswith(ext) for ext in extensoes):

                destino = os.path.join(pasta, pasta_destino)
                os.makedirs(destino, exist_ok=True)
                shutil.move(caminho_arquivo, os.path.join(destino, arquivo))
                print(f"{arquivo} movido para {pasta_destino}")
                contador += 1
                break

print(f"\n{contador} arquivos foram organizados com sucesso.")
