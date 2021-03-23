# Crie um programa que leia dois números e mostre
# a soma entre eles.

n1 = float(input('Digite um número '))
n2 = float(input('Digite outro '))
s = n1 + n2
cores = {'limpa': '\033[m',
         'magenta': '\033[1;35m',
         'amarelo': '\033[1;33m'}
print('A soma entre {}{}{} e {}{}{} é: {:.2f}'.format(cores['magenta'], n1, cores['limpa'], cores['amarelo'], n2, cores['limpa'], s))
