# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: EQUILATERO, ISOSCELES ou ESCALENO

reta1 = float(input("Informe o comprimento da primeira reta: "))
reta2 = float(input("Informe o comprimento da segunda reta: "))
reta3 = float(input("Informe o comprimento da terceira reta: "))

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print("Essas retas podem SIM formar um triangulo! :)")
    if reta1 == reta2 == reta3:
        print("E elas formarão um TRIANGULO EQUILÁTERO")
    elif (reta1 == reta2 and reta1 != reta3) or (reta1 == reta3 and reta1 != reta2):
        print("E elas formarão um TRIANGULO ISOSCELES")
    else:
        print("E elas formarão um TRIANGULO ESCALENO")
else:
    print("Infelizmente essas retas NÃO podem formar um triângulo... :(")