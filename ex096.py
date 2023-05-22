# Crie um programa que tenha uma função chamada AREA que receba as dimensões de um
# terreno retangular e mostre a area de um terreno

def area(l1,l2):
    a = l1 * l2
    print(f"A área de um terreno com {l1}m de largura e {l2}m de comprimento é de {a}m²")
print("~"* 30)
print(f"{'Calculador de área 2.0':^30}")
print("~"* 30)
area(float(input("Insira a largura do terreno (em metros): ")),float(input("Insira o comprimento do terreno (em metros): ")))
