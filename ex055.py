# Leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lidos
peso = []
for i in range(0,5):
    peso.append(float(input("Insira o peso da pessoa #{}: ".format(i+1))))

print(peso)

menor = 0
maior = 0

for j in range (0,5):
    for k in range (0, 5):
        if peso[j]<peso[k] and peso[j]<peso[menor]:
            menor = j

for l in range (0,5):
    for m in range (0, 5):
        if peso[l]>peso[m] and peso[l]>peso[maior]:
            maior = l

print("O menor peso registrado é o da Pessoa#{}, pesando {}kg.".format(menor+1, peso[menor]))
print("O maior peso registrado é o da Pessoa#{}, pesando {}kg.".format(maior+1, peso[maior]))