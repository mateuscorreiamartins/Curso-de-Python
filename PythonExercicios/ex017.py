# Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import sqrt
print('-' * 40)
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjcente: '))
h = co**2 + ca**2
print('A medida da hipotenusa é: {:.2f}.'.format(sqrt(h)))
print('-' * 40)
