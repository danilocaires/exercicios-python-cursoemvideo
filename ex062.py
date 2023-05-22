# Melhore o ex061 perguntando quantos termos o usuário quer ver, em sequencia. Com 0 o programa termina.

p1 = int(input("\nInsira o primeiro valor da sua PA: "))
rz = int(input("Insira a razão da sua PA: "))
c = 0
term = 10

while c < term and term != 0:
    print(p1, end=" ")
    p1 += rz
    c += 1
    if c == term:
        term = int(input("\n\nQuantos termos a mais da PA você gostaria de ver? "))+c

print("\nACABOU!\n")