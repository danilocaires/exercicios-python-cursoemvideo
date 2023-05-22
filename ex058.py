# Melhore o jogo do ex028 com o computador pensando um número entre 0 e 10. Agora o jogador vai chutar até adivinhar.
# No final o jogo mostra quantos palpites foram necessários

import random

num1 = random.randint(0,10)
num2 = 0
tries = 1

print("O programa está pensando em um número entre 0 e 10. Você consegue adivinhar qual? ")

while num1 != num2:
    num2 = int(input("Seu palpite: "))

    if num1 > num2:
        print("Maior... Tente novamente!")
        tries += 1
        
    elif num1 < num2:
        print("Menor... Tente novamente!")
        tries += 1
    else:
        print("Parabéns! O programa estava pensando no número {}. Você precisou de {} tentativa(s) para acertar.".format(num1, tries))
        