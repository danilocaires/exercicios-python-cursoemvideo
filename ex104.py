# crie um programa com uma função LEIA INT que só recebe inteiros

def leia_int(texto):
    """Lê um numero inteiro e notifica se o valor não for numero inteiro"""
    while True:
        i = str(input(texto))
        if  i.isnumeric():
            break
        print("\033[31mErro! Digite um int!\033[m")
    return i

n = leia_int("Digite um número: ")
print(f"Voce acabou de digitar o número {n}")