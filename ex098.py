# Crie um programa que tenha uma função CONTADOR
# e recebe 3 parametros: inicio, fim e passo
# teste com 3 contagens:
# 1 a 10 de 1 em 1
# 10 até 0 de 2 em 2
# personalizada

from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f"\nContando de {inicio} até {fim}, de {passo} em {passo}:")
    i = inicio
    sleep(2)
    if inicio < fim:
        while i <= fim:
            sleep(0.5)
            print(i, end=" ", flush=True)
            i += passo
    else:
        while i >= fim:
            sleep(0.5)
            print(i, end=" ", flush=True)
            i -= passo
    print("Pronto! :)\n")


contador(1, 10, 1)
contador(10, 0, 2)
print("\nVamos fazer uma contagem personalizada!")
contador(int(input("Qual o primeiro valor: ")), int(input(
    "Qual é o último valor: ")), int(input("Fazer a contagem de quanto em quanto: ")))
