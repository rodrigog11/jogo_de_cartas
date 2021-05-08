def extrai_naipe(x):
    if len(x) == 3:
        return x[2]
    elif len(x) == 2:
        return x[1]

def extrai_valor(x):
    if len(x) == 3:
        return x[0]+x[1] 
    if len(x) == 2:
        return x[0]

def lista_movimentos_possiveis(baralho, i):
    vazia=[]
    if i==0:
        return vazia
    if extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i-1]):
        vazia.append(1)
    if i >= 3:
        if extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-3]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i-3]):
            vazia.append(3)
    return vazia 

def empilha(baralho, o, d):
    if o > d and (o - d == 1 or o - d == 3):
        baralho[d] = baralho[o]
        del baralho[o]
    return baralho

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