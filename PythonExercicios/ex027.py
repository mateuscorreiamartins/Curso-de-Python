# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
# nome separadamente.

# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

n = str(input('Seu nome completo: ')).strip()
nome = n.split()
print('Prazer em te conhecer! ')
print('\nAnalisando seu nome... \n')
print('Seu primeiro nome é {}. '.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))
