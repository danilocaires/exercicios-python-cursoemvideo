# Faça um programa que leia um ano qualquer e mostre se ele é um ano BISSEXTO

ano = int(input("Insira o ano para saber se é um ano Bissexto ou não: "))

if (ano%4 == 0):
    print("{} É um ano Bissexto".format(ano))
else:
    print("{} NÃO É um ano Bissexto".format(ano))