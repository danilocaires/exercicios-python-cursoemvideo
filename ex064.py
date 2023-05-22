#  crie um programa que leia vários valores e no final mostre quantos valores foram digitados e qual a soma deles
# digite 999 para parar o programa e calcular

n = 0
c = -1
soma = 0

while n != 999:
    soma += n
    c += 1
    n = int(input("\nInsira um valor (digite 999 para encerrar): "))

print("Encerrando contagem:")
print("Você digitou {} valores e a soma entre todos eles é {}".format(c, soma))