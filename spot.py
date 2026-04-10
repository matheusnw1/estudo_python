import requests

def buscar_musicas(artista):
    lista = []
    musica = requests.get(f'https://itunes.apple.com/search?term={artista}&media=music&limit=5')
    dicionario = (musica.json())
    musicas = (dicionario['results'])
    for musica in musicas:
        music = (f'{musica['trackName']}')
        lista.append(music)
    return lista
