# Crie um programa que leia uma expressão numerica
# o programa deve analisar se os parenteses da expressão estão corretos
# (parenteses abertos e fechados corretamente)

expressão = str(input("Digite a expressão numérica a ser avaliada: "))
p_abertos = 0
message = "A expressão está \033[32mcorreta\033[m!"

for c in expressão:
    if c == "(":
        p_abertos += 1
    if c == ")":
        p_abertos -= 1
    if p_abertos < 0:
        message = "A expressão está \033[31merrada\033[m!"
        break

if p_abertos != 0:
        message = "A expressão está \033[31merrada\033[m!"
print(message)