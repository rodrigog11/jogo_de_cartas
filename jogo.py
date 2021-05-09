#Importando funções e arquivos a serem utilizados:
from funcoes import *

#Texto inicial - boas-vindas e instruções:
#(SUGESTÃO: uso da função 'time.sleep' para sugerir maior interatividade - COLOCAR A POSSIBILIDADE DE DAR SKIP DAS INSTRUÇÕES)
print("\033[1m" + "|Paciência Acordeão|\n" + "====================" +"\033[0m" + "\n" )
print("Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\n")
print("Existem apenas dois movimentos possíveis:\n" )
print ("1. Empilhar uma carta sobre a carta imediatamente anterior")
print("2. Empilhar uma carta sobre a terceira carta anterior.\n")
print("Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n")
print("1. As duas cartas possuem o mesmo valor ou")
print("2. As duas cartas possuem o mesmo naipe.\n")
print("Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\n")
#Input inicial (começa o jogo):
input("Aperte [ENTER] para para iniciar o jogo...")

#Igualando a lista retornada pela função 'cria_baralho' (um baralho) à lista 'baralho':
baralho = cria_baralho()

#Uso de estrutura de loop (while, for) junto à função 'possui_movimentos_possiveis' para averiguar se ainda há movimentos possíveis após o último movimento:
while possui_movimentos_possiveis(baralho):
    #Imprimindo o baralho
    numerador(baralho)
    
    #Armazenando a carta a ser movida na variável i (numerador da carta; não representa o índice):
    i = int(input('Escolha uma carta (digite um número entre 1 e {0}): '.format(len(baralho))))

    #No caso de i não corresponder a uma carta existente, perguntando novamente qual carta o/a jogador(a) deseja mover:
    #PRECISA CONECTAR ESSE WHILE/FOR COM O ELSE (SE NÃO FOR POSSÍVEL MOVER A CARTA)
        
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
        #TEM DE EXIBIR AS CARTAS DAS POSIÇÕES DE DESTINO, EXEMPLO: 1.(CARTA 1) \n 2.(CARTA 2) )
        onde_empilha = int(input('Sobre qual carta você quer empilhar {0}? '.format(baralho[i-1])))
        if onde_empilha == 1:
            empilhar = empilha(baralho,i-1 ,i-2)
            baralho = empilhar
        elif onde_empilha == 3:
            empilhar=empilha(baralho,i-1,i-4)
            baralho = empilhar

    #ESTE ELSE PRECISA SER CONECTADO COM O WHILE (DO INPUT DO I Ñ SER VÁLIDO) E COM A LISTA 'MOV'
    else:
        #Imprimindo mensagem referente à impossibilidade de mover a carta escolhida:
        i = int(input("A carta {0} não pode ser movida. Por favor, digite um número entre 1 e {1}: ".format(baralho[i-1], len(baralho))))

#Printando o estado final do baralho, quando houver nenhum movimento possível
print("{0} \n Não há mais movimentos possíveis.".format(baralho))

#Resultado do jogo:
if len(baralho) > 10:
    print("Você perdeu. {0} cartas foram eliminadas.".format( len(cria_baralho()) - len(baralho)))
#NÃO ACHO QUE TENHA PROBLEMA EM FAZER ISSO AQUI, MAS NÃO TENHO CERTEZA:
else:
    if len(baralho) > 5:
        print("Você chegou perto! {0} cartas foram eliminadas.".format(len(cria_baralho()) - len(baralho)))
    elif len(baralho) > 1:
        print("Você quase ganhou! {0} cartas foram eliminadas. Muito bem!".format(len(cria_baralho()) - len(baralho)))
    elif len(baralho) == 1:
        print("Você ganhou - "+ "\033[1m" + "parabéns!" + "\033[0m")
