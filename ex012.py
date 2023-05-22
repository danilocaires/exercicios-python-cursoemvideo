# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto

preco = float(input("Insira o preço original do produto: R$"))
desconto5 = preco - (preco * 5 / 100)
print(
    "O valor do produto com desconto de 5% é de : R${:.2f}".format(desconto5))
