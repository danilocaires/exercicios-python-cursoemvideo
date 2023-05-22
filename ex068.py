# Jogar par ou impar contra o computador
# O jogo só será interrompido quando o jogador perder
# No final mostrar quantas vezes o jogador tentou

from random import randint

pi = ""
cont = 0

while True:
    pi = ""
    jogador = -1
    while pi != "PAR" and pi != "IMPAR":
        pi = str(input("Par ou Impar? :")).upper()

    computador = randint(0,10)

    while jogador < 0 or jogador > 10:
        jogador = int(input("Quantos dedos (0 a 10)? :"))

    print(f"{computador}+{jogador}={jogador+computador}")

    if pi == "PAR":
        if (jogador+computador) % 2 == 0:
            print("Deu PAR!")
            print("Voce venceu! O computador quer uma revanche!")
            cont += 1
        else:
            print("Deu IMPAR!")
            break
    else:
        if (jogador+computador) % 2 == 0:
            print("Deu PAR!")
            break
        else:
            print("Deu IMPAR!")
            print("Voce venceu! O computador quer uma revanche!")
            cont += 1

print(f"O computador venceu essa. Você acumulou: {cont} vitória(s)!")