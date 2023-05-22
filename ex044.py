# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: – à vista dinheiro/cheque: 10% de desconto – à vista no cartão: 5% de desconto – em até 2x no cartão: preço formal – 3x ou mais no cartão: 20% de juros

valor = float(input("Insira o valor do produto: R$"))
forma = int(input("""Selecione a forma de pagamento da lista abaixo:
1 - À Vista no Dinheiro
2 - À Vista no Cartão
3 - 2x no Cartão
4 - 3x ou mais no cartão

Opção: """))

if forma == 1:
    print("O produto que custava R${:.2f} será pago à vista no dinheiro e com 10% off ele sai por R${:.2f}".format(valor,valor*0.9))
elif forma == 2:
    print("O produto que custava R${:.2f} será pago à vista no cartão e com 5% off ele sai por R${:.2f}".format(valor,valor*0.95))
elif forma == 3:
    print("O produto que custava R${:.2f} será pago no cartão em 2x então o seu valor continua o mesmo".format(valor))
elif forma == 4:
    print("O produto que custava R${:.2f} será pago no cartão em 3x ou mais e seu valor total aumenta para R${:.2f}".format(valor,valor*1.2))
else:
    print("Opção inválida. Selecione 1, 2, 3 ou 4.")