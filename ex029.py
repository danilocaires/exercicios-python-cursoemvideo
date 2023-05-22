# Escreva um programa que leia a velocidade de um carro. Se ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado e o valor da multa (considerando R$7 por cada km/h acima do limite)

velocidade = int(input("Informe a velocidade do carro: "))

if velocidade > 80:
    multa = (velocidade - 80)*7
    print("Veículo acima do limite de velocidade. Será multado no valor de R${:.2f}".format(multa))
else:
    print("Parabéns, continue respeitando os limites de velocidade da via.")