# Crie um programa que tenha uma função VOTO que recebe o ano de nascimento da pessoa e retorna se o voto é obrigatório ou não
# se < 18 ou > 60 = voto opcional

def voto(nasc):
    from datetime import date
    """Calcula se o voto da pessoa é obrigatório ou opcional."""
    idade = (date.today().year)-nasc
    if idade < 16:
        return f"Para você que tem {idade} anos, o voto é \033[31mNegado\033[m"
    elif idade < 18 or idade > 60:
        return f"Para você que tem {idade} anos, o voto é \033[32mOpcional\033[m"
    else:
        return f"Para você que tem {idade} anos, o voto é \033[36mObrigatório\033[m"

dataNasc = int(input("Insira o ano do seu nascimento: "))
print(voto(dataNasc))