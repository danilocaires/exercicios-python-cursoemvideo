def leiadinheiro(msg):
    valido = False
    while valido == False:
        p = str(input(msg))
        if p.isalpha():
            print(f"\033[31mErro! '{p}' não é um preço válido.\033[m")
        else:
            valido = True
            return float(p)