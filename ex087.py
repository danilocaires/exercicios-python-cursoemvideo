# aprimore o ex086 mostrando no final:
# a Soma dos valores pares, a soma dos valores da terceira coluna, o maior valor da segunda linha

rows = []
columns = []
somapares = 0

for c in range (0,3):
    for d in range(0,3):
        columns.append(int(input(f"Valor {c}x{d}: ")))
    rows.append(columns[:])
    columns.clear()

print("\nGerando matriz...")

for c in range (0,3):
    print("")
    for d in range(0,3):
        print(f"[\033[1m{rows[c][d]:^5}\033[m]",end="")
        if rows[c][d] % 2 == 0:
            somapares += rows[c][d]

somaterceira = rows[0][2] + rows[1][2] + rows [2][2]

print("\n")
print(f"A soma dos valores pares é: {somapares}")
print(f"A soma dos valores da terceira coluna é: {somaterceira}")
rows[1].sort(reverse=True)
print(f"O maior valor da segunda linha é: {rows[1][0]}")