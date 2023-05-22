# Faça um programa que leia o nome comprelo de uma pessoa mostrando o primeiro e o ultimo nome, separadamente

nome = input("Digite um nome: ").split()

print("O primeiro nome é: {}".format(nome[0]))
print("O último nome é: {}".format(nome[len(nome)-1]))
