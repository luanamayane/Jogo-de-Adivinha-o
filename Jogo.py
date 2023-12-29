import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        tentativa = int(input("Tente adivinhar o número secreto (entre 1 e 100): "))
        tentativas += 1

        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas!")
            break
        elif tentativa > numero_secreto:
            print("Tente um número menor.")
        else:
            print("Tente um número maior.")

jogo_adivinhacao()
