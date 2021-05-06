import random
def cria_baralho():
    naipes = ['♣', '♥', '♠', '♦']
    letras = ['A', 'J', 'Q', 'K']
    cartas = []
    baralho = []

    #preenchendo a lista 'cartas' com a numeração das cartas (sem naipes)
    for i1 in range (2, 11):
        cartas.append(str(i1))
    for i2 in range (4):
        cartas.append(letras[i2])
    
    #atribuindo os naipes às cartas e inserindo-as na lista 'baralho' (note que a ordem de j1 e j2 não importa, desde que cada índice se refira à lista correta)
    for j1 in range(4):
        for j2 in range(13):
            carta = cartas[j2] + naipes[j1]
            baralho.append(carta)
    
    #embaralhando o baralho
    random.shuffle(baralho)

    return baralho