#  Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
print('\n\033[1;30mVAI COMEÇAR A CONTAGEM REGRESSIVA!\033[m')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[1;33mB\033[1;31mO\033[1;30mO\033[1;36mO\033[1;37mO\033[1;34mO\033[1;32mM\033[m!!!')
