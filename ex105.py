# Faça um programa c/ uma função NOTAS que pode ler varias notas
# Essa função retorna um dicionário com as informações:
# qtde de notas, maior nota, menor nota, media turma e situação(bool)

def notas(* n,sit=False):
    mai = 0
    men = 0
    som = 0
    v = 0

    for x in n:
        som += x
        if x>mai or v==0:
            mai=x
        if x<men or v==0:
            men=x
        v = 1
    med = som/len(n)
    dic = {'total':len(n),'maior':mai,'menor':men,'media':med}
    if sit:
        if med >= 7:
            dic['situacao'] = "BOA"
        elif med >= 5:
            dic['situacao'] = "RAZOAVEL"
        else:
            dic['situacao'] = "RUIM"
    return dic


resp = notas(5, 7, 8.5, 9, 3, sit=True)
print(resp)