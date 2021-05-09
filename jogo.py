#Importando funções e arquivos a serem utilizados
import time
from funcoes import *

#Texto inicial - boas-vindas e instruções
#(uso da biblioteca time para sugerir maior interatividade)
time.sleep(0)
print("\033[1m" + "|Paciência Acordeão|\n" + "====================" +"\033[0m" + "\n" )
time.sleep(0)
print("Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. \n")
time.sleep(0)
print("Existem apenas dois movimentos possíveis: \n" )
time.sleep(0)
print ("1. Empilhar uma carta sobre a carta imediatamente anterior")
time.sleep(0)
print("2. Empilhar uma carta sobre a terceira carta anterior.\n")
time.sleep(0)
print("Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n")
time.sleep(0)
print("1. As duas cartas possuem o mesmo valor ou")
time.sleep(0)
print("2. As duas cartas possuem o mesmo naipe.\n")
time.sleep(0)
print("Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\n")
time.sleep(0)
#Input inicial (começa o jogo)
input("Aperte [ENTER] para para iniciar o jogo...")

#Igualando a lista retornada pela função 'cria_baralho' (um baralho) à lista 'baralho':
baralho = cria_baralho()

#Uso de estrutura de loop (while, for) junto à função 'possui_movimentos_possiveis' para averiguar se ainda há movimentos possíveis após o último movimento:
while possui_movimentos_possiveis(baralho):
    #Imprimindo o baralho
    numerador(baralho)
    
    #Armazenando a carta a ser movida na variável i (numerador da carta; não representa o índice):
    i = int(input('Escolha uma carta (digite um número entre 1 e {0}): '.format(len(baralho))))
    
    #Armazenando a lista de movimentos possíveis para a carta escolhida (i) na lista 'mov':
    mov = lista_movimentos_possiveis(baralho, i-1)

    #Se a lista mov tiver apenas um item: 
    if len(mov) == 1:
        if mov[0] == 1:
            empilhar = empilha(baralho, i-1, i-2)
            baralho = empilhar
        elif mov[0] == 3:
            empilhar = empilha(baralho, i-1, i-4)   
            baralho = empilhar

    #Se a lista mov tiver dois itens (ou mais):
    elif len(mov) > 1:
        onde_empilha = int(input('Sobre qual carta você quer empilhar {0}? '.format(baralho[i-1])))
        if onde_empilha == 1:
            empilhar = empilha(baralho,i-1 ,i-2)
            baralho = empilhar
        elif onde_empilha == 3:
            empilhar=empilha(baralho,i-1,i-4)
            baralho = empilhar

    else:
        #Imprimindo mensagem referente à impossibilidade de mover a carta escolhida:
        i = int(input("A carta {0} não pode ser movida. Por favor, digite um número entre 1 e {1}: ".format(baralho[i-1], len(baralho)))) 

#