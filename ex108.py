# Adapte o código do ex107 criando uma função adicional que formate os numeros para valores em R$

import moeda

valor = float(input("Digite um valor: R$"))
print(f"A metade de {moeda.rs(valor)} é {moeda.rs(moeda.metade(valor))}.")
print(f"O dobro de {moeda.rs(valor)} é {moeda.rs(moeda.dobro(valor))}")
print(f"Aumentando 10%, temos {moeda.rs(moeda.aumentar(valor,10))}")
print(f"Reduzindo 13%, temos {moeda.rs(moeda.diminuir(valor,13))}")