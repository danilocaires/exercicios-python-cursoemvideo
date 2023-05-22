# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

v1 = input('Digite algo: ')
print('O tipo primitivo desse valor é:\033[34m', type(v1), "\033[m")
print('É um ou mais espaços? \033[34m', v1.isspace(), "\033[m")
print('É alfanumérico? \033[34m', v1.isalnum(), "\033[m")
print('É alfabético? \033[34m', v1.isalpha(), "\033[m")
print('É decimal? \033[34m', v1.isdecimal(), "\033[m")
print('É minúsculo? \033[34m', v1.islower(), "\033[m")
print('É maiúsculo? \033[34m', v1.isupper(), "\033[m")
print('É um dígito? \033[34m', v1.isdigit(), "\033[m")
