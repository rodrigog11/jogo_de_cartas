import funcoes 
#texto inicial (menos importante agora)
print("\033[1m" + "|Paciência Acordeão|\n" + "====================" +"\033[0m" + "\n" )
print("Bem vindo(a) ao jogo 'Paciência Acordeão'. Seu objetivo é colocar todas as cartas sobre uma mesma pilha.")
print("Há dois movimentos possíveis: \n 1. Empilhar uma carta sobre a carta imediatamente anterior \n 2. Empilhar uma carta sobre a terceira carta anterior")
#definir a opção de iniciar ((pressione 'enter', digite 'ok' e afins))
baralho = funcoes.cria_baralho()
print(baralho)
#usar while/for enquanto houver jogadas possíveis
#input para o jogador escolher a carta que deseja mover
#usar a função da possibilidade de movimentar a carta
#exibir mensagem caso não seja possível mover a carta escolhida e voltar pro input
#usar a função da lista de movimentos
#usar a função empilha carta

while funcoes.possui_movimentos_possiveis(baralho) == True:
    qual_carta = input('Qual carta gostaria de empilhar?')
    i = 0
    while i < len(baralho):
        if qual_carta == baralho[i]:
            movimentos = funcoes.lista_movimentos_possiveis(baralho, i)
            if movimentos == [1]:
                empilhar = funcoes.empilha(baralho, i, i-1)
            elif movimentos == [1,3]:
                empilhar = funcoes.empilha(baralho, i, i-3)
            else:
                print('não há movimentos possíveis, escolha outra carta')
                break
        else: 
            i+=1


