# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep


print("\n\033[1m::: EMPRESTIMO CALCULATOR 1.0 :::\033[m\n")

valor = float(
    input("Qual o valor do imóvel que você gostaria de financiar? R$"))
salario = float(input("Qual é o seu salário atualmente? R$"))
anos = int(input("Em quantos anos você quer financiar o imóvel? Anos: "))

print("\n\033[1mCalculando...\033[m\n")
sleep(2)

if valor > (salario * 0.3) * (anos * 12):
    print("\033[31mLamentamos, mas o seu empréstimo não pôde ser aprovado. :(")
else:
    print("\033[32mEmpréstimo aprovado! Você vai pagar {} parcelas de R${:.2f}.\n\033[1mSUA ALMA É NOSSA PELOS PRÓXIMOS {} ANOS!!! MUAHAHAHAH\n".format(
        anos*12, valor/(anos*12), anos))
