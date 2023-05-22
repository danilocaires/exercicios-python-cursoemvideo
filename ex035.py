# Faça um programa que leia o comprimento de tres retas e diga ao usuario se elas podem formar um triangulo

reta1 = float(input("Informe o comprimento da primeira reta: "))
reta2 = float(input("Informe o comprimento da segunda reta: "))
reta3 = float(input("Informe o comprimento da terceira reta: "))

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print("Essas retas podem SIM formar um triangulo! :)")
else:
    print("Infelizmente essas retas NÃO podem formar um triângulo... :(")