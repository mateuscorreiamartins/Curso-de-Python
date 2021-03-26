# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
a = float(input('Digite um ângulo: '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print('O seno de {} é: {:.2f} '.format(a, seno))
print('O cosseno de {} é: {:.2f} '.format(a, cosseno))
print('A tangente de {} é: {:.2f} '.format(a, tangente))
