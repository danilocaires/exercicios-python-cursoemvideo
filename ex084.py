# programa que le nome e peso de varias pessoas
# no final mostre: quantas pessoas cadastradas, listagem das pessoas mais pesadas e listagem das pessoas mais leves

pessoas = []
cadastro = []
c = 0
maior = 0
menor = 0

while True:
    cadastro.append(str(input(f"Digite o nome da pessoa {c+1}: ")))
    cadastro.append(float(input(f"Digite o peso da pessoa {c+1}: ")))

    if c == 0 or cadastro[1]>pessoas[maior][1]:
        maior = c
    if c == 0 or cadastro[1]<pessoas[menor][1]:
        menor = c

    pessoas.append(cadastro[:])
    cadastro.clear()
    c += 1
    if str(input("Continuar cadastrando? S/N:")).upper() == "N":
        break

print(pessoas)

print(f"O número de pessoas cadastradas foi: {len(pessoas)} pessoas")
print(f"A pessoa mais pesada cadastrada foi {pessoas[maior][0]} com {pessoas[maior][1]}kg")
print(f"A pessoa mais leve cadastrada foi {pessoas[menor][0]} com {pessoas[menor][1]}kg")