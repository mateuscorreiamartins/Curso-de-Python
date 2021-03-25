# Faça um algoritmo que leia o salário de um 
# funcionário e mostre seu novo salário com 15% de aumento.

s = float(input('Digite o valor do seu salário: '))
a = (15 / 100) * s
print('O seu novo salário é: {}.'.format(a + s))
print('\n' * 2)
print('O seu novo salário é: {}.'.format((15 / 100) * s + s))
