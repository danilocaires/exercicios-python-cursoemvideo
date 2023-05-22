# Escreva um programa que converta uma temperatura digitada em °C e converta para °F

tempc = float(input('Digite a temperatura em °C: '))
tempf = tempc * (9/5) + 32
print('A temperatura em Celsius de {}°C convertida em Fahrenheit é de {}°F'.format(tempc, tempf))
