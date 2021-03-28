# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
# número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
print('Vou pensar em um número inteiro e você terá que adivinhar!\n ')
lista = [0, 1, 2, 3, 4, 5]
n = random.choice(lista)
num = int(input('Qual número de 0 a 5 eu estou pensando? '))
if num == n:
    print('Parabéns, você acertou! ')
else:
    print('Que pena, você errou. ')
