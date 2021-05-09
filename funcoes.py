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


def extrai_naipe(carta):
    #igualando a variável 'naipe' ao último caractere da string 'carta'
    naipe = carta[len(carta)-1]
    return naipe


def extrai_valor(carta):
    if len(carta) == 2:
        return carta[0]
    if len(carta) == 3:
        return carta[0] + carta[1] 


def lista_movimentos_possiveis(baralho, i):
    movimentos = []
    if i == 0:
        return movimentos
    if extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i-1]):
        movimentos.append(1)
    if i >= 3:
        if extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-3]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i-3]):
            movimentos.append(3)
    return movimentos 


def empilha(baralho, o, d):
    if o > d and (o - d == 1 or o - d == 3):
        baralho[d] = baralho[o]
        del baralho[o]
    return baralho


def possui_movimentos_possiveis(baralho):
    for posicao in range(len(baralho)):
        if lista_movimentos_possiveis(baralho, posicao) != []:
            return True
    return False


def numerador(baralho):
    for i in range(len(baralho)):
        print(str(i + 1) + ". " + baralho[i])


