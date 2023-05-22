# Crie um programa que leia dois números e mostre a soma entre eles

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
s = n1 + n2
print('A soma entre \033[33m{}\033[m e \033[33m{}\033[m é igual à: \033[1;32m{}'.format(n1, n2, s))
