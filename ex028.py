# Escreva um programa que pense em um número aleatório entre 0 e 5. O usuário deve tentar adivinhar o número e o programa deve informar se o usuário acertou ou não

import random

num1 = random.randint(0,5)
num2 = int(input("O programa está pensando em um número entre 0 e 5. Você consegue adivinhar qual? "))

if num1 == num2:
    print("Parabéns! O programa estava pensando no número {}.".format(num1))
else:
    print("Que pena, você errou. O programa estava pensando no número {}.".format(num1))