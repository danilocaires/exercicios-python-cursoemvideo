# Leia vários números. No final mostre:
# a media entre os valores, o maior valor, o menor valor
# O programa fica perguntando para o user quando ele quer parar

n = 0
soma = 0
maior = 0
menor = 0
c = 0
pare = "N"

while pare == "N":
    n = int(input("\nInsira um valor: "))
    soma += n
    if c == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c += 1
    pare = input("\nDeseja encerrar a contagem? (S/N): ").upper()

media = soma/c

print("\nEncerrando contagem:")
print("\nA média entre os valores digitados é {}".format(media))
print("O maior valor digitado foi {}".format(maior))
print("O menor valor digitado foi {}\n".format(menor))