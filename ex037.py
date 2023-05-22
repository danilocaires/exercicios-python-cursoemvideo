# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

from time import sleep

print("\n\033[1m::: Conversor de Base :::\033[m\n")

decimal = int(input("Insira o número que você deseja converter: "))
base = int(input("""Escolha a base para a qual você quer converter o número \033[1m{}\033[m:
1 = BINÁRIO
2 = OCTAL
3 = HEXADECIMAL

Opção: """.format(decimal)))
print("\nCalculando...\n")
sleep(2)

if base == 1:
    print("O número {} se converte para \033[1m{}\033[m em \033[1;31mBINÁRIO\033[m".format(decimal,bin(decimal)[2:]))
elif base == 2:
    print("O número {} se converte para \033[1m{}\033[m em \033[1;32mOCTAL\033[m".format(decimal,oct(decimal)[2:]))
elif base == 3:
    print("O número {} se converte para \033[1m{}\033[m em \033[1;33mHEXADECIMAL\033[m".format(decimal,hex(decimal)[2:]))
else:
    print("Escolha uma das opções disponíveis de base (1, 2 ou 3)")