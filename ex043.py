# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: – IMC abaixo de 18,5: Abaixo do Peso – Entre 18,5 e 25: Peso Ideal – 25 até 30: Sobrepeso – 30 até 40: Obesidade – Acima de 40: Obesidade Mórbida

print("\n::: IMC Calculator Tabajara :::\n")
peso = float(input("Insira o seu peso: "))
altura = float(input("Insira a sua altura: "))

imc = peso / pow(altura, 2)

if imc <= 18.5:
    print("IMC: {:.2f} - ABAIXO DO PESO".format(imc))
elif imc <= 25:
    print("IMC: {:.2f} - PESO IDEAL".format(imc))
elif imc <= 30:
    print("IMC: {:.2f} - SOBREPESO".format(imc))
elif imc <= 40:
    print("IMC: {:.2f} - OBESIDADE".format(imc))
else:
    print("IMC: {:.2f} - OBESIDADE MORBIDA".format(imc))
