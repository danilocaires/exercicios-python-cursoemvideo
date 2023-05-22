def aumentar(p, porc, rs=False):
    np = p+(p * porc / 100)
    if rs:
        return f"R${np:.2f}"
    else:
        return np


def diminuir(p, porc, rs=False):
    np = p-(p * porc / 100)
    if rs:
        return f"R${np:.2f}"
    else:
        return np


def dobro(p, rs=False):
    if rs:
        return f"R${p*2:.2f}"
    else:
        return p*2


def metade(p, rs=False):
    if rs:
        return f"R${p/2:.2f}"
    else:
        return p/2


def rs(p):
    return f"R${p:.2f}"


def resumo(p, aum=0, dim=0):
    print("=-"*17)
    print(f"{'RESUMO DO VALOR':^35}")
    print("=-"*17)
    print(f"Preço analisado: \t{rs(p)}")
    print(f"Dobro do preço: \t{dobro(p, True)}")
    print(f"Metade do preço: \t{metade(p, True)}")
    print(f"{aum}% de aumento: \t{aumentar(p,aum, True)}")
    print(f"{dim}% de redução: \t{diminuir(p,dim, True)}")
    print("=-"*17)