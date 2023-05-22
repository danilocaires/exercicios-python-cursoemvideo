# leia: idade e sexo de varias pessoas
# a cada cadastro confirmar se deseja continuar
# No final mostrar: quantas pessoas tem mais de 18 anos, quantos homens cadastrados, quantas mulheres tem menos de 20 anos
c = 1
maior = 0
homens = 0
mulheres20 = 0

while True:
    sexo = ""
    print(f"\n::::: Pessoa {c} :::::")
    idade = int(input("Idade: "))
    while sexo != "M" and sexo != "F":
        sexo = str(input("Sexo (M/F): ")).upper()
    if idade>=18:
        maior += 1
    if sexo == "M":
        homens += 1
    if idade < 20 and sexo == "F":
        mulheres20 += 1
    if input("Deseja continuar cadastrando? (S/N): ").upper() == "N":
        break
    c += 1

print(f"\nAnalisando {c} cadastros...\n")
print(f"-> {maior} pessoas cadastradas tem mais de 18 anos")
print(f"-> {homens} pessoas cadastradas são homens")
print(f"-> {mulheres20} pessoas cadastradas são mulheres com menos de 20 anos\n")
