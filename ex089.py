# Leia nome e duas notas de varios alunos
# No final mostre um boletim contendo a media de cada um e permita ao usuaria mostrar as notas de cada aluno individualmente

aluno = []
classe = []
c = 0

while True:
    print(f"--- Aluno nº{c+1} ---")
    aluno.append(str(input("Nome: ")))
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))
    classe.append(aluno[:])
    aluno.clear()
    c += 1
    if input("Continuar cadastro? S/N: ").upper() == "N":
        break

print("\n::: BOLETIM FINAL :::\n")
for c, d in enumerate(classe):
    print(f"Aluno {c+1}: {d[0]:10} Média: {(d[1]+d[2])/2}")

while True:
    n = int(input("\nQual aluno você deseja verificar as notas? (0 para sair):"))
    if n == 0:
        break
    print(f" Aluno {n}: {classe[n-1][0]:10} Nota 1: {classe[n-1][1]:<5} Nota 2: {classe[n-1][2]:<5} Média: {(classe[n-1][1]+classe[n-1][2])/2}")
print("\nEncerrando o programa\n")