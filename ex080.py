# O user digita 5 valores numéricos
# O programa já cadastra os valores na posição correta na lista
# NÃo pode usar o sort()
# No final mostre a lista

valores = []
c = 0
novovalor = 0

while c < 5:
    novovalor = int(input(f"Insira o {c+1}o valor: "))
    d = 0
    while d < len(valores):
        if novovalor <= valores[d]:
            valores.insert(d,novovalor)
            break
        elif d == len(valores)-1:
            valores.append(novovalor)
            break
        else:
            d += 1
    if c == 0:
        valores.append(novovalor)
    c += 1

print(f"Os valores digitados em ordem são: {valores}")