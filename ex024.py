# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = input("Digite o nome da cidade: ")


if ((cidade.split())[0].upper() == "SANTO"):
    print("O nome da cidade COMEÇA com 'Santo'")
else:
    print("O nome da cidade NÃO COMEÇA com 'Santo'")
