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
quer_jogar = input('Deseja jogar? digite sim ou nao')

if quer_jogar == 'sim':
    jogar = True 
else: 
    jogar = False
while jogar:

    baralho = cria_baralho()
    
    while possui_movimentos_possiveis(baralho):

        print (numerador(baralho))
        i = 0
        for i in range(len(baralho)):
            qual_carta = int(input('Qual carta gostaria de empilhar? escolha um numero'))
            if qual_carta == i+1:
                movimentos = lista_movimentos_possiveis(baralho, i+1)
                if movimentos == [1]:
                    empilhar = empilha(baralho, i+1, i)
                    baralho = empilhar
                elif movimentos == [3]:
                    empilhar = empilha(baralho, i+1, i-2)
                    baralho = empilhar
                elif movimentos == [1,3]:
                    qual_empilha = input("Deseja empilhar a carta sobre a carta 1 ou a carta 3 anterior? ")
                    if qual_empilha == "1":
                        empilhar = empilha(baralho, i+1, i)
                        baralho = empilhar
                    elif qual_empilha == "3":
                        empilhar = empilha(baralho, i+1, i-2)
                        baralho = empilhar
                else:
                    print('escolha outra carta')
            else:
                i+=1


            
















 
            '''if qual_carta == i+1:
                movimentos = lista_movimentos_possiveis(baralho, i+1)
                if movimentos == [1]:
                    empilhar = empilha(baralho, i+1, i)
                    baralho = empilhar
                elif movimentos == [3]:
                    empilhar = empilha(baralho, i+1, i-2)
                    baralho = empilhar
                elif movimentos == [1, 3]:
                    qual_empilha = input("Deseja empilhar a carta sobre a carta 1 ou a carta 3 anterior? ")
                    if qual_empilha == "1":
                        empilhar = empilha(baralho, i+1, i)
                        baralho = empilhar
                    elif qual_empilha == "3":
                        empilhar = empilha(baralho, i+1, i-2)
                        baralho = empilhar
                else:
                    print('não há movimentos possíveis, escolha outra carta')
                
            else: 
                i+=1'''