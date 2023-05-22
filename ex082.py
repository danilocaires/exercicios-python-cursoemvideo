# Leia varios valores e coloque em uma lista
# depois crie mais duas listas, uma para valores pares e outra para impares
# No fim mostre as 3 listas

novonumero = 0
numeros = []
pares = []
impares = []

while True:
    novonumero = int(input("Digite um número: "))
    numeros.append(novonumero)
    if novonumero % 2 == 0 and novonumero != 0:
        pares.append(novonumero)
    elif novonumero % 2 != 0:
        impares.append(novonumero)
    if str(input("Deseja continuar? S/N: ")).upper() == "N":
        break

print(f"Todos os valores digitados: {numeros}")
print(f"Valores digitados que são PARES: {pares}")
print(f"Valores digitados que são IMPARES: {impares}")