# o programa ajuda o jogador a criar palpites na megasena
# O programa pergunta quantos jogos
# O programa gera x conjuntos de 6 numeros (1 a 60)
# 
from random import randint
from time import sleep

print("\n\nMEGASENA NUMERO GENERATOR 1.0\n")

numjogos = int(input("Quantos jogos você deseja fazer? :"))
cartela = []
jogo = []

for c in range(0,numjogos):
    while len(jogo) <= 6:
        novonum = randint(1,60)
        if novonum not in jogo:
            jogo.append(novonum)
    jogo.sort()
    cartela.append(jogo[:])
    jogo.clear()

print("\nGerando jogos...\n")

for c in range(0,numjogos):
    sleep(1)
    print(f"Jogo {c+1}: ",end="")
    for d in range(0,6):
       print(cartela[c][d], end=" ")
    print("")

print("\nBoa sorte!!\n")