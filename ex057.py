# Leia o sexo da pessoa e só aceite os valores "M" ou "F". Peça novamente até ter um valor correto

sexo = " "

while sexo != "M" and sexo != "F":
    sexo = input("Por favor informe seu sexo (M/F): ").upper()
    if sexo != "M" and sexo != "F":
        print("\033[31mValor inválido. Favor digitar 'M' para Masculino ou 'F' para feminino.\033[m")

print("\033[32mValor computado com sucesso! Sexo: {}\n\033[m".format(sexo))