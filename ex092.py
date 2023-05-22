# leia NOME, NASCIMENTO e CARTEIRA DE TRABALHO
# guarde nome, idade e ctps
# se ctps != de 0, ler tbm ano de contrataçao e salario
# Calcule com quantos anos a pessoa vai se aposentar
# (35 anos de contribuição p aposentar)

from datetime import date

cadastro = {}

cadastro['nome'] = str(input("Nome: "))
cadastro['idade'] = date.today().year - int(str(input("Data de Nascimento (DD/MM/AAAA): "))[-4:])
cadastro['ctps'] = int(input("Carteira de Trabalho (se não possui, digite 0): "))
if cadastro['ctps'] != 0:
    cadastro['ano_contr'] = int(input("Ano da contratação: "))
    cadastro['salário'] = float(input("Salário: R$"))

print(f"O {cadastro['nome']} tem {cadastro['idade']} anos ", end="")
if cadastro['ctps'] != 0:
    print(f"e vai se aposentar em {35-(date.today().year-cadastro['ano_contr'])} anos (em {cadastro['ano_contr']+35}).\n")
else:
    print("e não trabalha.\n")
