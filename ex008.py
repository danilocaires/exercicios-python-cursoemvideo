# Escreva um programa que leia um valor em metro e o exiba convertido em centímetros e milímetros

m = float(input('Digite uma distância em Metros: '))
print('A distância em Metros de {}m corresponde à:'.format(m))
print('{}km'.format(m/1000))
print('{:.0f}cm'.format(m*100))
print('{:.0f}mm'.format(m*1000))
