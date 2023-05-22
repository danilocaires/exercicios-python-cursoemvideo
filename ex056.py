# Faça um programa que leia o nome, idade e sexo de 4 pessoas. No final mostrar:
# - A média da idade do grupo - Qual o nome do homem mais velho - Quantas mulheres tem menos de 20 anos

from time import sleep

nome = []
idade = []
sexo = []

for i in range(0, 4):
    nome.append(input("Nome (pessoa #{}): ".format(i+1)))
    idade.append(int(input("Idade: ")))
    sexo.append(input("Sexo(M ou F): "))

media_idade = (idade[0]+idade[1]+idade[2]+idade[3])/4

idade_mais_alta = 0
mais_velho = 0

for j in range(0, 4):
    if idade[j] > idade_mais_alta:
        idade_mais_alta = idade[j]
        mais_velho = j

mulheres_menos_20 = 0

for k in range(0, 4):
    if sexo[k] == "F" and idade[k] < 20:
        mulheres_menos_20 = mulheres_menos_20 + 1

print("Analisando pessoas...\n")
sleep(2)

print("""\nDados finais:
        - A média das idades é de {:.2f} anos.
        - O homem mais velho do grupo é o {} com {} anos
        - O número de mulheres com menos de 20 anos é de: {}""".format(media_idade, nome[mais_velho], idade_mais_alta, mulheres_menos_20))
