#  Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
dec = int(input('''[ 1 ] converter para \033[1;34mBINÁRIO\033[m
[ 2 ] converter para \033[1;33mOCTAL\033[m
[ 3 ] converter para \033[1;36mHEXADECIMAL\033[m\n'''))
if dec == 1:
    print('O número {} em binário é {}'.format(n, bin(n)[2:]))
elif dec == 2:
    print('O número {} em octal é {}'.format(n, oct(n)[2:]))
elif dec == 3:
    print('O número {} em hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('\033[4;31mÉ 1, 2 ou 3, seu cabeçudo!')
