# crie uma tupla com nome e preço de produtos respectivamente
# organize e mostre o resultado em uma tabela

tupla = ("Lapis", 4.50, "Borracha", 6, "Caderno", 23.90, "Régua", 15,"Transferidor", 20.50)
c = 0

print("-"*40)
print(f"{'LISTA DE MATERIAIS':^40}")
print("-"*40)

while c < len(tupla):
    print(f"{tupla[c]:.<30}",end="")
    c += 1
    print(f"R${tupla[c]:>7.2f}")
    c += 1

print("-"*40)