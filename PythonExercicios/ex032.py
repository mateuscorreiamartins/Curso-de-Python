# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Qual é o ano? '))
b = ano % 4
if b == 0:
    print('\033[1;36mO ano de {} é bissexto. '.format(ano))
else:
    print('\033[1;31mO ano de {} não é bissexto. '.format(ano))
