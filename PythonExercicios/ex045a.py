# Crie um programa que faça o computador 
# jogar Jokenpô com você.

import random
from time import sleep
print('\033[7;30m{:^55}\033[m'.format('=' * 50))
print('\033[4;36m{:^55}'.format('VAMOS JOGAR JOKENPÔ'))
print('\033[7;30m{:^55}\033[m'.format('=' * 50))
esc = int(input('\n\n\033[1;30mEscolha 1 para Pedra, 2 para Papel ou 3 para Tesoura:\033[m '))
