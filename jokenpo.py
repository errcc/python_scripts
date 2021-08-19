import random

#Função que traduz o número associado à CPU a um dos componentes do jogo
def escolha_cpu(x):
    if x == 1:
        return "Pedra"
    elif x == 2:
        return "Papel"
    else:
        return "Tesoura"

#Função que compara as escolhas do jogador e da CPU
def compara(jogador,cpu):
    if jogador == 1:
        if cpu == 3:
            return True
    elif jogador == 2:
        if cpu == 1:
            return True
    elif jogador == 3:
        if cpu == 2:
            return True
    return False

#while x != 
print("Digite o número correspondente a sua opção:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")
choice_user = input() #captura a resposta do usuário
choice_cpu = random.randint(1,3) #gera a escolha da CPU
#print(choice_cpu)
print("O computador escolheu ",escolha_cpu(choice_cpu))
if int(choice_user) == choice_cpu: #Mostra se a partida ficar empatada
    print("Empate")
elif compara(int(choice_user),choice_cpu) == True: #int(choice_user) supr importante, pq input() captura como char
    print("Você venceu!")
else:
    print("Você perdeu")



#print(compara(1,1))
        