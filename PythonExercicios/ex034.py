# Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento.

# Para salários superiores a R$1.250,00, calcule um aumento de 10%.

# Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('\033[34mQual o valor do seu salário? R$\033[m'))
if s > 1250:
    a1 = (s * 10 / 100) + s
    print('\033[1;32mO seu novo salário é: R${}'.format(a1))
else:
    a2 = (s * 15 / 100) + s
    print('\033[1;32mO seu novo salário é: {}'.format(a2))
