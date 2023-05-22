# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: – Até 9 anos: MIRIM – Até 14 anos: INFANTIL – Até 19 anos: JÚNIOR – Até 25 anos: SÊNIOR – Acima de 25 anos: MASTER

import datetime


ano_nasc = int(input("\nInsira o ano do seu nascimento: "))

idade = datetime.date.today().year - ano_nasc

if idade <= 9:
    print("\nDe acordo com a CNN, sua categoria de natação é \033[31mMIRIM\033[m.")
elif idade <= 14:
    print("\nDe acordo com a CNN, sua categoria de natação é \033[32mINFANTIL\033[m.")
elif idade <= 19:
    print("\nDe acordo com a CNN, sua categoria de natação é \033[33mJUNIOR\033[m.")
elif idade <= 25:
    print("\nDe acordo com a CNN, sua categoria de natação é \033[34mSENIOR\033[m.")
else:
    print("\nDe acordo com a CNN, sua categoria de natação é \033[35mMASTER\033[m.")