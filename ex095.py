# aprimore o ex093
# para que ele funcione para varios jogadores

from time import sleep


jogadores = []
jogador = {}
gols = []
detalhe = 0

while True:
    jogador['nome'] = str(input("\nNome do jogador: "))
    jogador['partidas'] = int(input("Número de partidas: "))
    for c in range (1,jogador['partidas']+1):
        gols.append(int(input(f"Gols na partida {c}: ")))
    jogador['gols'] = gols[:]
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    if str(input("Continuar cadastrando? S/N: ")).upper() == "N":
        break

while True:
    sleep(3)
    print("\n::: TABELA GERAL DE JOGADORES! :::\n")
    for c in range(0, len(jogadores)):
        print(f"Jogador {c+1}: {jogadores[c]['nome']}", end=" ")
        print(f"- Gols: {sum(jogadores[c]['gols'])}")
    detalhe = int(input("\n> Qual jogador você gostaria de ver os detalhes? (0 para sair) : "))-1
    if detalhe == -1:
        print("\nEncerrando o programa...\n")
        break
    if detalhe >= len(jogadores):
        print(f"Erro! Não existe jogador número {detalhe+1}")
    else:
        print("\n")
        print("+"*45)
        print(f"Jogador: {jogadores[detalhe]['nome']}")
        print(f"Numero de partidas: {jogadores[detalhe]['partidas']}")
        for d, e in enumerate(jogadores[detalhe]['gols']):
            print(f"Gols na partida {d+1}: {e}")
        print(f"A soma dos gols desse jogador é de: {sum(jogadores[detalhe]['gols'])} gol(s).")
        print("+"*45)