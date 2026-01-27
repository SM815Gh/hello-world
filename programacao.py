import random

def jogo_adivinhacao():
    print("🎯 Bem-vindo ao jogo de adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("Tente adivinhar o número entre 1 e 100.")

    while not acertou:
        try:
            chute = int(input("Digite seu palpite: "))
            tentativas += 1

            if chute < numero_secreto:
                print("🔼 O número secreto é maior!")
            elif chute > numero_secreto:
                print("🔽 O número secreto é menor!")
            else:
                print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas!")
                acertou = True

        except ValueError:
            print("❌ Por favor, digite um número válido.")

if __name__ == "__main__":
    jogo_adivinhacao()