#Importando funções e arquivos a serem utilizados:
from funcoes import *

#Texto inicial - boas-vindas e instruções:
#(SUGESTÃO: uso da função 'time.sleep' para sugerir maior interatividade - COLOCAR A POSSIBILIDADE DE DAR SKIP DAS INSTRUÇÕES)
print(cores.bold + "|Paciência Acordeão|\n" + "====================" + cores.reset + "\n" )
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


continuar = True
#Uso de estrutura de loop (while, for) junto à função 'possui_movimentos_possiveis' para averiguar se ainda há movimentos possíveis após o último movimento:
while continuar:
    #Igualando a lista retornada pela função 'cria_baralho' (um baralho) à lista 'baralho':
    baralho = cria_baralho()

    while possui_movimentos_possiveis(baralho):
        #Imprimindo o baralho
        numero_e_cor(baralho)

        pergunta = True

        while pergunta:
        #Armazenando a carta a ser movida na variável i (numerador da carta; não representa o índice):
            i = int(input('Escolha uma carta (digite um número entre 1 e {0}): '.format(len(baralho))))
            if 0 < i <= len(baralho):
                pergunta = False
            else: 
                pergunta = True
                print('Numero inválido, escreva um numero entre 1 e {0}' .format(len(baralho)))
        #No caso de i não corresponder a uma carta existente, pergunta novamente qual carta o/a jogador(a) deseja mover:
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
            #Exibindo as cartas sobre as quais é possível empilhar a carta escolhida e perguntando para onde o/a jogador(a) deseja movê-la:
            onde_empilha = int(input('Sobre qual carta você quer empilhar {0}?\n1.{1}\n2.{2}\n\nDigite o número de sua escolha(1-{3}):  '.format(baralho[i-1], baralho[i-2], baralho[i-4], len(baralho))))
            if onde_empilha == 1:
                empilhar = empilha(baralho,i-1 ,i-2)
                baralho = empilhar
            elif onde_empilha == 2:
                empilhar=empilha(baralho,i-1,i-4)
                baralho = empilhar
            
            #PRECISA DE ELSE (CASO O Nº Ñ SEJA 1 OU 2): UM LOOP ATÉ O USUÁRIO DIGITAR UM VALOR VÁLIDO PARA onde_empilha

        #ESTE ELSE PRECISA SER CONECTADO COM O WHILE (DO INPUT DO I Ñ SER VÁLIDO) E COM A LISTA 'MOV'
        else:
            #Imprimindo mensagem referente à impossibilidade de mover a carta escolhida:
            print("A carta {0} não pode ser movida. ".format(baralho[i-1]))

    #Printando o estado final do baralho, quando houver nenhum movimento possível
    print("{0} \n Não há mais movimentos possíveis.".format(baralho))

    #Resultado do jogo:
    if len(baralho) > 10:
        print("Você perdeu. {0} cartas foram eliminadas.".format( len(cria_baralho()) - len(baralho)))
    #NÃO ACHO QUE TENHA PROBLEMA EM FAZER ISSO AQUI, MAS NÃO TENHO CERTEZA:
    elif len(baralho) > 5:
        print("Você chegou perto! {0} cartas foram eliminadas.".format(len(cria_baralho()) - len(baralho)))
    elif len(baralho) > 1:
        print("Você quase ganhou! {0} cartas foram eliminadas. Muito bem!".format(len(cria_baralho()) - len(baralho)))
    elif len(baralho) == 1:
        print("Você ganhou - "+ "\033[1m" + "parabéns!" + "\033[0m")

    #PRECISA DE UM LOOP AQUI:
    jogar = input("Quer jogar novamente? digite sim ou nao ")
    if jogar == 'sim'
        continuar = True
    else:
        continuar = False
        print('Obrigado por jogar!')

