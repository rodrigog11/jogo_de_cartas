import funcoes
#texto inicial (menos importante agora)
print("\033[1m" + "|Paciência Acordeão|\n" + "====================" +"\033[0m" + "\n" )
print("Bem vindo(a) ao jogo 'Paciência Acordeão'. Seu objetivo é colocar todas as cartas sobre uma mesma pilha.")
print("Há dois movimentos possíveis: \n 1. Empilhar uma carta sobre a carta imediatamente anterior \n 2. Empilhar uma carta sobre a carta imediatamente anterior")
#definir a opção de iniciar ((pressione 'enter', digite 'ok' e afins))
print(funcoes.cria_baralho())
#usar while/for enquanto houver jogadas possíveis
#input para o jogador escolher a carta que deseja mover
#usar a função da possibilidade de movimentar a carta
#exibir mensagem caso não seja possível mover a carta escolhida e voltar pro input
#usar a função da lista de movimentos
#usar a função empilha carta
