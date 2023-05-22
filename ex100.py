# Faça um programa c/ uma lista chamada NUMEROS e duas funçoes chamadas SORTEIA e SOMAPAR
# a primeira sorteia 5 numeros e coloca na lista
# a segunda vai mostrar a soma entre todos os valores pares da lista

from random import randint
from time import sleep


def sorteia(lista):
    print("Sorteando 5 números aleatórios: ")
    i = 0
    while i < 5:
        nv = randint(0,9)
        sleep(0.5)
        print(nv,end=" ",flush=True)
        lista.append(nv)
        i += 1
    print("Pronto!")

def somapar(lista):
    print("Somando os números pares da lista:",lista)
    soma = 0
    i = 0
    while i < len(lista):
        if lista[i]%2 == 0:
            soma += lista[i]
        i += 1
    print("O valor da soma dos pares é:",soma)

numeros = []
print("")
sorteia(numeros)
print("")
somapar(numeros)
print("")