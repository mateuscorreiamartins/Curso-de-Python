# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Qual o comprimento da primeira reta? '))
r2 = float(input('Qual o comprimento da segunda reta? '))
r3 = float(input('Qual o comprimento da terceira reta? '))
if r3 < r1+ r2 and r2 < r1 + r3 and r1 < r2 + r3:
    print('\033[1;32mIsso pode ser um triângulo.\033[m ')
else:
    print('\033[1;31mIsso não pode ser um triângulo. ')
