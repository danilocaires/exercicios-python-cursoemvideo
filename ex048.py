# calcule a soma entre todos os numeros impares múltiplos de 3 entre 1 e 500
soma = 0
for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c
print("A soma entre todos os numeros impares múltiplos de 3 entre 1 e 500 é: {}".format(soma))