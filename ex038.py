# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: – O primeiro valor é maior – O segundo valor é maior – Não existe valor maior, os dois são iguais

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

if n1 > n2:
    print("\nO primeiro número é o maior!\n")
elif n2 > n1:
    print("\nO segundo número é maior!\n")
else:
    print("\nOs dois números são iguais!\n")