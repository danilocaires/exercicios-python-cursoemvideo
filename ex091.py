# Crie um programa em que 4 jogadores joguem um dado e tenha resultados aleatórios e guarde os resultados em um dicionário. No final, coloque o dicionário em ordem sabendo que  o vencedor tirou o maior numero no dado

from random import randint
from operator import itemgetter

jogo = {}

jogo['Jogador 1'] = randint(1,6)
jogo['Jogador 2'] = randint(1,6)
jogo['Jogador 3'] = randint(1,6)
jogo['Jogador 4'] = randint(1,6)

print("\nValores sorteados:")

for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(ranking)

print("::: RANKING DOS JOGADORES :::")
for i, j in enumerate(ranking):
    print(f"{i+1}o lugar: {j[0]} com {j[1]}")
print("")