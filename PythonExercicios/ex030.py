# Crie um programa que leia um número inteiro e mostre na tela
# se ele é PAR ou ÍMPAR.

num = int(input('Qual o número? '))
a = num % 2
if a > 0:
    print('Esse número é ÍMPAR! ')
else:
    print('Esse número é PAR! ')
