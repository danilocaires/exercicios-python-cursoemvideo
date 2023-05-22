# Leia varios numeros e coloque em uma lista:
# Mostrar: quantos numeros foram digitados, a lista de valores ordenada de forma decrescente, se o valor 5 foi digitado e esta na lista ou nao

numeros = []

while True:
    numeros.append(int(input("Digite um número: ")))
    if str(input("Deseja continuar? S/N: ")).upper() == "N":
        break

print(f"\nForam digitados {len(numeros)} valores.")
numeros.sort(reverse=True)
print(f"Os valores listados na ordem decrescente são: {numeros}")
if 5 in numeros:
    print("O número 5 está na lista!\n")
else:
    print("O numero 5 não está na lista...\n")