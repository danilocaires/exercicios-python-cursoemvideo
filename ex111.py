# Crie um pacote chamado utilidades que tenha dois módulos (moeda e dado).
# Transfira as funções dos exercicios anteriores para o modulo MOEDA

from utilidades import moeda

valor = float(input("Digite um valor: R$"))
moeda.resumo(valor, 80, 35)