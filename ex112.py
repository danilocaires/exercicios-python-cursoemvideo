# No módulo DADO do pacote UTILIDADES, crie uma função chamada leiadinheiro que receba um valor e valide se esse valor é monetário

from utilidades import moeda,dado

valor = dado.leiadinheiro("Digite um valor: R$")
moeda.resumo(valor, 80, 35)