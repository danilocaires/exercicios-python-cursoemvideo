# crie uma tupla totalmente preenchida entre 0 e 20.
# o programa le um numero e retorna o nome do numero em extenso

extenso = ("Zero","Um","Dois","Três","Quatro",
"Cinco","Seis","Sete","Oito","Nove","Dez","Onze",
"Doze","Treze","Quatorze","Quinze","Dezesseis",
"Dezessete","Dezoito","Dezenove","Vinte")

while True:
    n = -1
    while n not in range(0,20):
        n = int(input("Digite um número \033[1mentre 0 e 20\033[m para exibir seu nome em extenso: "))

    print(extenso[n])

    if input("Deseja continuar? (S/N):").upper() == "N":
        break