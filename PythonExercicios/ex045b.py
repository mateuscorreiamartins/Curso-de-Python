# O QUE O GUANABARA FEZ

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('\nQual a sua jogada? '))
print('\nJO')
sleep(1.3)
print('KEN')
sleep(1.3)
print('PÔ\n')
print('-=' * 14)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 14)