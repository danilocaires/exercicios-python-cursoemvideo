# Programa que leia o nome e media de um aluno, guardando a situaçao. No final mostre nome, media e se está aprovado ou reprovado

aluno = {}

aluno['nome'] = str(input("Nome do aluno: "))
aluno['media'] = float(input("Média do aluno: "))
if aluno["media"] >= 7:
    aluno['situacao'] = "\033[32mAprovado"
elif aluno["media"] < 7 and aluno["media"] >= 5:
    aluno['situacao'] = "\033[33mRecuperação"
else:
    aluno['situacao'] = "\033[31mReprovado"

print("\nRelatório final:")
print(f"Nome do aluno: {aluno['nome']}")
print(f"Média do aluno: {aluno['media']}")
print(f"Situação do aluno: {aluno['situacao']}\n")