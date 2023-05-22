# Reescreva a função LEIAINT que fizemos no desafio 104, incluindo a possibilidade da digitação de um tipo inválido.
# Crie também a função LEIAFLOAT com a mesma funcionalidade

def leia_int(msg):
    """Lê um numero inteiro e notifica se o valor não for numero inteiro"""
    while True:
        try:
            n = int(input(msg))
        except:
            print("\033[31mErro! Digite um int!\033[m")
        else:
            return n

def leia_float(msg):
    """Lê um numero real e notifica se o valor não for numero real"""
    while True:
        try:
            n = float(input(msg))
            if n == None:
                print("\033[31mO usuário não escolheu um float.\033[m")
                return 0
        except:
            print("\033[31mErro! Digite um float!\033[m")
        else:
            return n

i = leia_int("Digite um número inteiro (int): ")
f = leia_float("Digite um número real (float): ")
print(f"Voce acabou de digitar o int {i} e o float {f:.2f}")