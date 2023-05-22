# Desenvolva um programa que pergunte a distancia de uma viagem (em Km) e calcule o preço da passagem (R$0,50/Km para viagens até 200Km e R$0,45/Km para viagens mais longas)

dist = float(input("Qual a distância da viagem a ser feita? "))

if (dist <= 200):
    preco = dist * 0.50
else:
    preco = dist * 0.45

print("O valor da passagem é de R${:.2f}".format(preco))
