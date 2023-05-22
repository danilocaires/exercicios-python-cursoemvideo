# Faça um programa que leia o nome de quatro alunos e determine a ordem de quem vai apresentar o trabalho primeiro

from random import shuffle


n1 = input("Nome do primeiro aluno: ")
n2 = input("Nome do segundo aluno: ")
n3 = input("Nome do terceiro aluno: ")
n4 = input("Nome do quarto aluno: ")

alunos = [n1,n2,n3,n4]

shuffle(alunos)

print("A ordem de apresentação dos trabalhos vai ser: ")
print(alunos)