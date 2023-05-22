# Crie uma função FATORIAL que receba dois parametros: o numero e se vai mostrar o processo do cálculo ou não

def fatorial(numero=1, processo=False):
    """-> Calcula o fatorial do numero desejado
    numero(int): o numero do qual deseja o fatorial
    processo(bool): se deseja ver o calculo ou não
    """
    f = 1
    for x in range(numero, 0, -1):
        if processo:
            print(x, end="")
            if x != 1:
                print(" x ", end="")
        f *= x
    if processo:
        print(" = ",end="")
    return f

print(fatorial(1,True))