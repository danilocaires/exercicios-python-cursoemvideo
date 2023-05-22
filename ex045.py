# JO KEN PO!

from random import randint
from time import sleep

item = (" ","Pedra", "Papel", "Tesoura")

jogador = int(input("""\nEscolha entre as opções:

1 - Pedra
2 - Papel
3 - Tesoura

Sua escolha: """))

computador = randint(1,3)

sleep(1)
print("\nJO\n")
sleep(1)
print("KEN\n")
sleep(1)
print("PO!\n")
sleep(1)

if (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
    print("\n\033[1mVocê venceu!\033[m Você escolheu {} e o computador escolheu {}\n".format(item[jogador],item[computador]))
elif (computador == 1 and jogador == 3) or (computador == 2 and jogador == 1) or (computador == 3 and jogador == 2):
    print("\n\033[1mO computador venceu!\033[m Você escolheu {} e o computador escolheu {}\n".format(item[jogador],item[computador]))
else:
    print("\n\033[1mEmpate!\033[m Você escolheu {} e o computador também escolheu {}\n".format(item[jogador],item[computador]))