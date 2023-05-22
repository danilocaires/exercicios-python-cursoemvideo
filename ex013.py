# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Insira o salário atual do funcionário: R$'))
aumento = float(
    input('Insira a porcentagem do aumento que o funcionário irá receber: %'))
salarionovo = salario + (salario * aumento / 100)
print('O funcionário que recebia R${:.2f} e recebeu um aumento de {}% agora vai passar a receber R${:.2f}'.format(
    salario, aumento, salarionovo))
