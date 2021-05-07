def empilha(baralho, o, d):
    if o > d and (o - d == 1 or o - d == 3):
        baralho[d] = baralho[o]
        del baralho[o]
    return baralho