import random

def joga():
    print("*********************************")
    print("Bem vindo ao jogo da Adivinhação!")
    print("*********************************")
    print("")
    print("Esse é um jogo que você deverá adivinhar qual número pensei")
    print("entre 0 e 100. Você terá 10 chances para acertar. Siga as dicas!")
    print("")

    print("Você poderá escolher entre 3 níveis:")
    print("(1) Fácil   (2) Médio   (3) Difícil")
    nivel = int(input("Em qual nível vc prefere jogar?"))
    if (nivel == 1):
        numero_tentativas = 20
    elif (nivel == 2):
        numero_tentativas = 10
    else:
        numero_tentativas = 5

    numero_secreto = random.randrange(0, 101)
    pontos = 100

    for tentativas in range (1, numero_tentativas + 1):
        print("Tentativa {} de {}.". format(tentativas, numero_tentativas))
        chute = input("Digite qual seu palpite: ")
        print("Você digitou o número: ", chute)
        numero = int(chute)
        if(numero >= 0 and numero <= 100):
            acerto = numero_secreto == numero
            maior = numero_secreto > numero
            menor = numero_secreto < numero
            if(acerto):
                print("Parabéns, você acertou e fez {} pontos!".format(pontos))
                break
            else:
                if (maior):
                    print("O número secreto é maior que {}".format(numero))
                    print("Infelizmente não foi dessa vez. Tente novamente!")
                    print(" ")
                elif (menor):
                    print("O número secreto é menor que {}".format(numero))
                    print("Infelizmente não foi dessa vez. Tente novamente!")
                    print(" ")
                pontos = pontos - abs(numero_secreto - numero)
        else:
            print("Você perdeu uma tentativa!")
            continue
    if not (acerto):
        print("O número pensado foi o ", numero_secreto)

    print("Fim do jogo!!!")

if (__name__ == "__main__"):
    joga()