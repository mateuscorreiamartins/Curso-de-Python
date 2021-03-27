# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas as letras minúsculas;
# Quantas letras ao tod0(sem considerar os espaços);
# Quantas letras têm o primeiro nome.

nome = input('Nome completo: ').strip()
print(' \nAnalisando seu nome... ')
print('O seu nome em maiúsculas é {}. '.format(nome.upper()))
print('O seu nome em minúscular é {}. '.format(nome.lower()))
print('O seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras. '.format(separa[0], len(separa[0])))
