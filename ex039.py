# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

print("\n\033[1m::: MILITAR CALCULATOR 3001.1 :::\033[m\n")

nascimento = int(input("Digite o ano do seu nascimento: "))
atual = datetime.date.today().year
idade = atual-nascimento

print("Quem nasceu em {} tem {} anos em {}.".format(nascimento,idade,atual))

if nascimento+18 == atual:
    print("Hora de se alistar, jovem!!")
elif nascimento+18 < atual :
    print("Espero que você tenha se alistado há {} anos!".format(atual-(nascimento+18)))
    print("Seu alistamento foi em {}".format(nascimento+18))
else:
    print("Você ainda tem {} anos antes de precisar se alistar. Aproveite!".format((nascimento+18)-atual))
    print("Seu alistamento vai ser em {}".format(nascimento+18))