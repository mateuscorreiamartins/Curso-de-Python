# Faça um programa que leia a largura e a 
# altura de uma parede em metros.
# Calcule a sua área e a quantidade de
# tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m².

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
area = a * l
print('A quantidade de tinta necessária para pintar sua parede é: {} litros.'.format(area / 2))
