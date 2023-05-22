# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com aumento
# Para salarios superiores a R$1.250,00, 10% de aumento. Para salários inferiores, 15%

salario = float(input("Digite o salário atual do funcionário: R$"))

if (salario >= 1250):
    aumento = salario * 0.15
else:
    aumento = salario * 0.1

print("O novo salário do funcionário após o aumento será de: R${}".format(salario+aumento))