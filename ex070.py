# o programa le o nome e preco de vários produtos, o programa pergunta a cada produto se o usuário quer continuar
# ao final mostrar: o valor total da compra, quantos produtos custam mais de 1000 reais, e qual o nome do produto mais barato

c = 1
total = 0
maisdemil = 0
nomebarato = ""
valorbarato = 0

while True:
    print(f"\n::::: Produto {c} :::::")
    nome = str(input("Nome: "))
    valor = float(input("Valor: "))
    total += valor
    if c == 1 or valor < valorbarato:
        nomebarato = nome
        valorbarato = valor
    if valor > 1000:
        maisdemil += 1
    if input("\nDeseja passar mais produtos? (S/N): ").upper() == "N":
        break
    c += 1

print("\nAnalisando compra cadastrada...\n")
print(f"-> O valor total da compra é de R${total}.")
print(f"-> {maisdemil} produto(s) custam mais de R$1000 reais.")
print(f"-> O produto mais barato da compra foi: {nomebarato}\n")