# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
ano = int(input('Qual o ano do seu nascimento? '))
idade = atual - ano
print('Que legal! Você tem {} anos.'.format(idade))
if idade <= 9:
    print('\nVocê está na \033[4;32mCATEGORIA MIRIM!\033[m')
elif idade <= 14:
    print('\nVocê está na \033[4;30mCATEGORIA INFANTIL!\033[m')
elif idade <= 19:
    print('\nVocê está na \033[4;33mCATEGORIA JÚNIOR!\033[m')