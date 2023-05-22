# Faça um programa com uma função chamada ESCREVA que recebe um texto qualquer e mostre linhas acima e abaixo do tamanho adequado

def escreva(texto):
    tamanho = len(texto)+4
    print("")
    print("~"*tamanho)
    print(f"  {texto}")
    print("~"*tamanho)
    print("")

escreva(input("\nEscreva um texto pra ele ficar bonitinho: "))