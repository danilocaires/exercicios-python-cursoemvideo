# crie um programa que leia o nome, numero de partidas e numero de gols em cada partida.
# Mostre toda a estrutuda detalhada e o total de gols

jogador = {}
gols = []

jogador['nome'] = str(input("Nome do jogador: "))
jogador['partidas'] = int(input("Número de partidas: "))
for c in range (1,jogador['partidas']+1):
    gols.append(int(input(f"Gols na partida {c}: ")))
jogador['gols'] = gols[:]
jogador['total'] = sum(jogador['gols'])
print("\n","="*30)
print(jogador)
print("="*30)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("="*30)
print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")
for c, d in enumerate(jogador['gols']):
    print(f"Gols na partida {c+1}: {d}")
print(f"A soma dos gols desse jogador é de: {jogador['total']} gol(s).\n")