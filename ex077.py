# cria uma tupla com varias palavras
# mostre as vogais em cada palavra da tupla

palavras = ("Zero","Um","Dois","Tres","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez")

for c in palavras:
    print(f"Na palavra {c} temos: ", end = "")
    i = 0
    while i < len(c):
        if c[i].lower() in ("aeiou"):
            print(c[i], end = " ")
        i += 1
    print("")