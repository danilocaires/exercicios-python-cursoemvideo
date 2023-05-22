# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (US$1 = R$3,27)

rs = float(input('Quanto você ganha por mês? R$'))
print('Bacana, mas se fosse em DOLAR (US${:.2f}) você ia tá ganhando R${:.2f}! AIIIIIII CHAMPS'.format(
    rs, rs*5.26))
