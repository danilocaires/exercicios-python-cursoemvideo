# Adicione ao módulo MOEDA.py uma função RESUMO que mostre todas as informações exibidas nos outros exercicios em uma função só

import methods.moeda as moeda

valor = float(input("Digite um valor: R$"))
moeda.resumo(valor, 80, 35)