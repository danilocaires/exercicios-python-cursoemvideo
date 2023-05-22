# Leia o ano de nascimento de sete pessoas e diga quantos atingiram a maioridade e quantos ainda não

import datetime

nasc = []
for i in range(1,8):
    nasc.append(int(input("Insira o ano de nascimento da pessoa #{}: ".format(i))))

atual = datetime.date.today().year

print(nasc)

maior = 0
menor = 0

for j in range(0,7):
    if nasc[j]+18>atual:
        menor += 1
    else:
        maior += 1

print("""\nNo grupo de pessoas inserido temos:
        - {} pessoas que ainda não atingiram a maioridade
        - {} pessoas que já atingiram a maioridade""".format(menor,maior))