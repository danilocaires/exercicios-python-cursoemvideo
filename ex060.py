# Leia um número e mostre o seu fatorial
# ex: 5! = 5x4x3x2x1 = 120

num = int(input("Insira um número para exibir seu fatorial: "))
fact = num

print("{}! = ".format(num),end="")

while num != 0:
    print(num, end="")
    if num != 1:
        print(end="x")
    if num != fact:
        fact = fact * num
    num -= 1

print(" = {}".format(fact))