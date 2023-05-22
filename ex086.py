# crie uma matriz  de dimensão 3x3 e preencha com valores do teclado
# No final mostre a matriz na tela

rows = []
columns = []

for c in range (0,3):
    for d in range(0,3):
        columns.append(int(input(f"Valor {c}x{d}: ")))
    rows.append(columns[:])
    columns.clear()

print("\nGerando matriz...\n")

for c in range (0,3):
    for d in range(0,3):
        print(f"[\033[1m{rows[c][d]:^5}\033[m]",end="")
    print()
print("\n")