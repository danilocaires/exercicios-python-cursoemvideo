# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado (Carro por dia: R$60 / KM rodado: R$0.15)

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos kms foram rodados com o carro? '))
valor = (dias * 60) + (km * 0.15)
print('Por {} dia(s) de aluguel e {}km(s) rodado(s) o valor total a ser pago pelo aluguel do carro é de R${:.2f}'.format(dias, km, valor))
