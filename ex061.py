# Refaça o ex051 usando while

p1 = int(input("Insira o primeiro valor da sua PA: "))
rz = int(input("Insira a razão da sua PA: "))
c = 0

while c < 10:
    print(p1, end=" ")
    p1 += rz
    c += 1

print("ACABOU!")