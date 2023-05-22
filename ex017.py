# Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
from math import hypot

cat_op = float(input("Informe o comprimento do primeiro cateto: "))
cat_ad = float(input("Informe o comprimento do segundo cateto: "))

hip = hypot(cat_op,cat_ad)

print("O comprimento da hipotenusa é: {:.2f}".format(hip))