# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessária para pintá-la (1L de tinta pinta 2m²)

l = float(input('Insira a largura da sua parede: '))
a = float(input('Insira a altura da sua parede: '))
print('A medida da sua parede é de {}x{}.\nA área total a ser pintada é de {:.2f}m².\nVocê vai precisar de {:.3f}L de tinta.'.format(l, a, l*a, (l*a)/2))
