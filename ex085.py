# digita 7 valores numericos e cadastre em uma unica lista com duas listas com numeros pares e impares dentro
# No final mostre os valores pares e impares em ordem crescente
numeros = [[],[]]
novovalor = 0

for c in range (0,7):
    novovalor = int(input(f"Digite o {c+1}o valor: "))
    if novovalor % 2 == 0:
        numeros[0].append(novovalor)
    else:
        numeros[1].append(novovalor)

numeros[0].sort()
numeros[1].sort()

print(f"Os valores pares digitados foram: {numeros[0]}")
print(f"Os valores impares digitados foram: {numeros[1]}")