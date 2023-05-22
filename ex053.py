# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo (desconsiderando os espaços)

frase = input("Digite uma frase para verificar se ela forma um palíndromo ou não: ")
frase = frase.replace(" ","")
frase = frase.upper()

frase_rev = ""
for c in range(len(frase)-1, -1, -1):
    frase_rev = frase_rev + frase[c]

if frase == frase_rev:
    print("\n\033[32;1mEssa frase é um palíndromo! :)\n")
else:
    print("\n\033[31;1mEssa frase não é um palíndromo. :(\n")