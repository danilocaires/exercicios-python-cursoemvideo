# Leia 5 valores e guarde em uma lista.
# retorne: o maior e menor valores digitados e suas posições na lista

valores = []
c = 0
maior = 0
maiorp = 0
menor = 0
menorp = 0

while c<5:
    valores.append(int(input(f"Digite o {c+1}o valor:")))
    if c == 0 or valores[c] > maior:
        maior = valores[c]
    if c == 0 or valores[c] < menor:
        menor = valores[c]
    c += 1

print(f"\nO maior número digitado foi o {maior} nas posições: ", end="")
for i, j in enumerate(valores):
    if j == maior:
        print(f"{i+1}...", end="")  
print(f"\nO menor número digitado foi o {menor} nas posições: ", end="")
for i, j in enumerate(valores):
    if j == menor:
        print(f"{i+1}...", end="")
print()