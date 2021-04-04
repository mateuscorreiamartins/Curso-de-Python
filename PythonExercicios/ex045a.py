# Crie um programa que faça o computador 
# jogar Jokenpô com você.

import random
from time import sleep
print('\033[7;30m{:^55}\033[m'.format('=' * 50))
print('\033[4;36m{:^55}'.format('VAMOS JOGAR JOKENPÔ'))
print('\033[7;30m{:^55}\033[m'.format('=' * 50))
esc = int(input('\n\n\033[1;30mEscolha 1 para Pedra, 2 para Papel ou 3 para Tesoura:\033[m '))
lista = [1, 2, 3]
comp = random.choice(lista)
print('\nJO')
sleep(1.1)
print('KEN')
sleep(1.1)
print('PÔ\n')
if esc == 1 and comp == 1 or esc == 2 and comp == 2 or esc == 3 and comp == 3:
    print('\033[1;33mEu escolhi {}.\033[m'.format(comp))
    print('\n\033[1;33mEMPATE!\033[m')
elif esc == 1 and comp == 2 or esc == 2 and comp == 3 or esc == 3 and comp == 1:
    print('\033[1;36mEu escolhi {}.\033[m'.format(comp))
    print('\n\033[1;31mVOCÊ PERDEU, VACILÃO!\033[m')
elif esc == 1 and comp == 3 or esc == 2 and comp == 1 or esc == 3 and comp == 2:
    print('\033[1;31mEu escolhi {}.\033[m'.format(comp))
    print('\n\033[1;36mPARABÉNS, VOCÊ VENCEU!\033[m')
