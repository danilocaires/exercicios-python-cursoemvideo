# faça um programa que tenha uma função MAIOR que receba vários valores e diga qual é o maior

from time import sleep


def maior(valores):
    print("~"*45)
    print("Analisando os valores passados:")
    i = 0
    while i < len(valores):
        print(valores[i],end=" ",flush=True)
        sleep(0.5)
        i += 1
    valores.sort(reverse=True)
    print(f"\nDos {len(valores)} valores inseridos, o maior valor é: ",valores[0])
    print("~"*45)
    sleep(2)

maior([0,45,12,6,44,2])
maior([345,6,0,-1,6,2,2,3])
maior([23,23])
maior([6])
maior([10000000000000000,1])
maior([6,6,6])