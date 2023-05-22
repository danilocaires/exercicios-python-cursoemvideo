# Faça um programa que leia um numero entre 0 e 9999 e mostre na tela cada um dos dígitos separados

numero = input("Insira um número entre 0 e 9999: ")

print("""Dissecando o número:
Unidades: {}
Dezenas: {}
Centenas: {}
Milhares: {}""".format(numero[3], numero[2], numero[1], numero[0]))
