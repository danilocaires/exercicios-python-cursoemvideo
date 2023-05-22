# Faça um programa que leia uma frase e mostre:
# Quantas vezes aparece a letra A, Em que posição ela aparece a primeira vez, Em que posição ela aparece a ultima vez

frase = input("Digite uma frase: ").upper()

print("Vezes que a letra A aparece: {}".format(frase.count("A")))
print("Posição que a letra A aparece pela primeira vez: {}".format(frase.find("A")))
print("Posição que a letra A aparece pela última vez: {}".format(frase.rfind("A")))
