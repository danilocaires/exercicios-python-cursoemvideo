# leia 4 valores no teclado e guarde em uma tupla
# mostre: quantas vezes apareceu o  valor 9, em que posição foi digitado o valor 3, a quantidade de numeros pares digitados

tupla = (int(input("Primeiro valor: ")),int(input("Segundo valor: ")),int(input("Terceiro valor: ")),int(input("Quarto valor: ")))

pares = 0

for c in tupla:
    if c % 2 == 0:
        pares += 1

print("\nAnalisando os valores digitados...\n")
print(f"-> O valor '9' apareceu {tupla.count(9)} vezes.")
if 3 in tupla:
    print(f"-> O número '3' aparece na {tupla.index(3)+1}a posição.")
else:
    print(f"-> O número '3' não aparece em nenhuma posição.")
print(f"-> A quantidade de numeros pares digitados é de {pares}.")