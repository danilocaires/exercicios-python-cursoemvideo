# Crie um nome que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas, O nome com todas as letras minúsculas, Quantas letras tem ao todo, Quantas letras tem o primeiro nome

nome = str(input("Digite um nome: ")).strip()
primeiro_nome = nome.split()

print("""Nome com todas as letras maiúsculas: {}
Nome com todas as letras minúsculas: {}
Quantidade de letras ao todo: {}
Quantas letras tem o primeiro nome: {}""".format(nome.upper(), nome.lower(), len("".join(primeiro_nome)),len(primeiro_nome[0])))
