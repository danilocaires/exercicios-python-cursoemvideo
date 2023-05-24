# Crie um modulo chamado MOEDA.py que tenha as funções:
# aumentar, diminuir, dobro e metade.
# Faça um programa que use essas funções

import methods.moeda as moeda

valor = float(input("Digite um valor: R$"))
print(f"A metade de {valor} é {moeda.metade(valor)}.")
print(f"O dobro de {valor} é {moeda.dobro(valor)}")
print(f"Aumentando 10%, temos {moeda.aumentar(valor,10)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(valor,13)}")
