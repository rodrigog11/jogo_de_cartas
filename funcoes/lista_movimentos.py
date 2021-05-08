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