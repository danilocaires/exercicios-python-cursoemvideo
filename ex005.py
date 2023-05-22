# Faça um programa que leia um numeori inteiro e mostre na tela o seu sucessor e seu antecessor

n1 = int(input('Digite um número: '))
print('Analisando o número {}: Seu antecessor é o \033[35m{}\033[m e o seu sucessor é o \033[35m{}\033[m.'.format(
    n1, n1-1, n1+1))
