# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão

p1 = int(input("Insira o primeiro valor da sua PA: "))
rz = int(input("Insira a razão da sua PA: "))
p10 = p1 + (10 -1)*rz

for c in range(p1,p10+rz,rz):
    print(c, end=" ")
print("ACABOU!")