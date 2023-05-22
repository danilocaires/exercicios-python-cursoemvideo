# O user digita vários valores numéricos e adicione em uma lista
# Caso o numero já exista, ele nao vai ser adicionado
# No final mostrar a lista em ordem crescente

valores = []
novovalor = 0
while True:
    novovalor = int(input("Digite um valor: "))
    if novovalor not in valores:
        valores.append(novovalor)
        print("Valor adicionado.")
    else:
        print("Valor repetido e não será adicionado.")
    if str(input("Deseja continuar: (S/N):")).upper() == "N":
        break
valores.sort()
print("Valores digitados em ordem crescente: ")
print(f"\nValores digitados: {valores}\n")