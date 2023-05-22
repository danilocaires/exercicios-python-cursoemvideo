# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc

real = float(input("Insira um número: "))
print("A parte inteira do número {} é {}".format(real,trunc(real)))