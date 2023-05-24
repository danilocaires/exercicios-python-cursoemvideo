# Modifique as funções do ex107 para que recebam um parametro a mais.
# Esse parametro opcional deve dizer se o retorno do metodo já vem formatado como dinheiro ou não

import methods.moeda as moeda

valor = float(input("Digite um valor: R$"))
print(f"A metade de {moeda.rs(valor)} é {moeda.metade(valor,True)}.")
print(f"O dobro de {moeda.rs(valor)} é {moeda.dobro(valor, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(valor,10, True)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(valor,13,True)}")