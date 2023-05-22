# Faça um programa que leia seis numeros inteiros e calcule a soma daqueles que forem PARES
n = []
soma = 0
for c in range(0,6):
    n.append(int(input("Insira um número: ")))
    if n[c] % 2 == 0:
        soma = soma + n[c]

print("\nA soma entre os números PARES é: \033[32;1m{}!".format(soma))