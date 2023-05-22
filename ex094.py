# Leia: nome, sexo e idade de várias pessoas
# cada pessoa em um dicionário e e todos em uma lista
# Mostre: quantas pessoas cadastradas, media de idade do grupo, lista com todas mulheres, lista com todos com idade acima da media

pessoas = []
cadastro = {}
c = 1
soma = 0
media = 0
mulheres = []
acima = []

while True:
    print(f"\nPessoa {c}")
    cadastro['nome'] = str(input("Nome: "))
    while True:
        cadastro['sexo'] = str(input("Sexo M/F: ")).upper()
        if cadastro['sexo'] in "MF":
            break
        print("Erro! Por favor digite M ou F.")
    cadastro['idade'] = int(input("Idade: "))
    soma += cadastro['idade']
    pessoas.append(cadastro.copy())
    cadastro.clear
    while True:
        mais_pessoas = input("Cadastrar mais pessoas? S/N: ").upper()
        if mais_pessoas in "SN":
            break
        print("Erro! Por favor digite S ou N")
    if mais_pessoas == "N":
        break
    c += 1

media = soma/len(pessoas)

for x in range(0, len(pessoas)):
    if pessoas[x]['sexo'] == "F":
        mulheres.append(pessoas[x]['nome'])
    if pessoas[x]['idade'] >= media:
        acima.append(pessoas[x]['nome'])

print(f"\nTotal de pessoas cadastradas: {len(pessoas)}")
print(f"Media da idade do grupo: {media}")
print(f"Todas as mulheres: {mulheres}")
print(f"Todos com idade acima da média: {acima}\n")
