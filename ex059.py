# Leia dois números e mostre um menu:
# SOMAR; MULTIPLICAR; MAIOR; MENOR; NOVOS NUMEROS; SAIR;

from time import sleep

opcao = 5
n1 = 0
n2 = 0

while opcao != 6:

    if opcao == 5:
        n1 = float(input("\nInsira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))

    sleep(1)

    print("""\n::: Menu interativo :::

    Número 1: {}
    Número 2: {}

    [ 1 ] Somar os números
    [ 2 ] Multiplicar os números
    [ 3 ] Qual número é maior?
    [ 4 ] Qual número é menor?
    [ 5 ] Reinserir números
    [ 6 ] Sair

:::::::::::::::::::::::\n""".format(n1,n2))

    opcao = int(input("\nSua opção: "))

    if opcao == 1:
        print("A soma entre os dois números é igual à: {}".format(n1+n2))
    if opcao == 2:
        print("O resultado da multiplicação entre os dois números é igual à: {}".format(n1*n2))
    if opcao == 3:
        if n1>n2:
            print("Dentre os dois números o maior numero é: {}".format(n1))
        elif n2>n1:
            print("Dentre os dois números o maior numero é: {}".format(n2))
        else:
            print("Os dois números são iguais. Não existe um número maior.")

    if opcao == 4:
        if n1<n2:
            print("Dentre os dois números o menor numero é: {}".format(n1))
        elif n2<n1:
            print("Dentre os dois números o menor numero é: {}".format(n2))
        else:
            print("Os dois números são iguais. Não existe um número menor.")

    if opcao > 6 or opcao < 1:
        print("Opção inválida. Por favor selecione uma opção entre 1 e 6.")

print("\nEncerrando o programa...\n")
