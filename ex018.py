# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

from math import sin, cos, tan, radians

ang = float(input("Insira o valor do ângulo: "))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print("O angulo de {} tem o SENO de {:.2f}, COSSENO de {:.2f} e TANGENTE de {:.2f}".format(ang,seno,cosseno,tangente))