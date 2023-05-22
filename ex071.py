# Crie um programa que simula o saque de um caixa eletronico
# leia o valor a ser sacado
# retorne quantas cédulas serão usadas (cédulas de 50, 20, 10, 5 e 1)

valor = int(input("\nQual o valor do saque? :R$"))

c50 = valor // 50
valor = valor % 50
c20 = valor // 20
valor = valor % 20
c10 = valor // 10
c1 = valor % 10

print(f"\nAqui está o seu saque:")
if c50>0:
    print(f"-> {c50} notas de R$50")
if c20>0:
    print(f"-> {c20} notas de R$20")
if c10>0:
    print(f"-> {c10} notas de R$10")
if c1>0:
    print(f"-> {c1} notas de R$1")
print("\n")