from funcoes import *


#texto inicial (menos importante agora)
print("\033[1m" + "|Paciência Acordeão|\n" + "====================" +"\033[0m" + "\n" )
print("Bem vindo(a) ao jogo 'Paciência Acordeão'. Seu objetivo é colocar todas as cartas sobre uma mesma pilha.")
print("Há dois movimentos possíveis: \n 1. Empilhar uma carta sobre a carta imediatamente anterior \n 2. Empilhar uma carta sobre a terceira carta anterior")

#definir a opção de iniciar ((pressione 'enter', digite 'ok' e afins)): COMPLEXO
#Numerar as cartas de 1 a 52 e printá-las (associar cada item da lista)


#usar while/for enquanto houver jogadas possíveis
#input para o jogador escolher a carta que deseja mover
#usar a função da possibilidade de movimentar a carta
#exibir mensagem caso não seja possível mover a carta escolhida e voltar pro input
#usar a função da lista de movimentos
#usar a função empilha carta
quer_jogar = input('Deseja jogar? digite sim ou nao: ')

if quer_jogar == 'sim':
    jogar = True 
else: 
    jogar = False
while jogar:

    baralho = cria_baralho()

    while possui_movimentos_possiveis(baralho):
        numerador(baralho)
        qual_carta = int(input('Qual carta quer escolher? '))
        i = qual_carta
        movimentos = lista_movimentos_possiveis(baralho,i-1)
        if len(movimentos)==1:
            if movimentos[0]==1:
                empilhar=empilha(baralho,i-1,i-2)
                baralho = empilhar
            else:
                empilhar=empilha(baralho,i-1,i-4)   
                baralho = empilhar

        elif len(movimentos)>1:
            qual_empilha = input('Gostaria de empilhar a carta escolhida sobre a anterior ou 3 anteriores? ')
            if qual_empilha == '1':
                empilhar=empilha(baralho,i,i-1)
                baralho = empilhar
            elif qual_empilha=='3':
                empilhar=empilha(baralho,i-1,i-4)
                baralho = empilhar
        else:
            print("Não há movimentos para realizar, escolha outra carta.") 
    
   