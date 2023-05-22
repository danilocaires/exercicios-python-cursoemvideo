# Faça um programa que leia o nome do jogador, o numero de gols e mostre essa informação na tela
# use funções e a função deve poder receber valores nulos

def ficha_jogador(nome="<username>",gols="0"):
    """Mostra o nome e a quantidade de gols de um jogador"""
    if nome == "":
        nome = "<username>"
    if gols == "":
        gols = "0"
    return f"O jogador {nome} fez {gols} gols no campeonato."

print(ficha_jogador(str(input("Nome do jogador: ")),
str(input("Numero de gols no campeonato: "))))