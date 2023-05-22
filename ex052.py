# Leia um numero inteiro e diga se ele é primo ou não

num = int(input("Digite um número para verificar se ele é primo ou não: "))
primo = 0

for c in range (1,num+1):
    if num % c == 0:
        primo = primo+1
        print("\033[34m", end="")
    else:
        print("\033[31m", end="")
    print(c, end=" ")
print("\033[m")

if primo == 2:
    print("O número {} é SIM um número PRIMO.".format(num))
else:
    print("O número {} NÃO é um número PRIMO.".format(num))