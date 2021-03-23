# Faça um programa que leia algo digitado no teclado
# e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

a = input('Digite algo: ')
print('\033[1;31m\nO tipo primitivo disso é: ', type(a))
print('\033[1;37mSó tem espaços? ', a.isspace())
print('\033[1;33mÉ um número? ', a.isnumeric())
print('\033[1;30mÉ alfabético? ', a.isalpha())
print('\033[1;35mÉ alfanumérico? ', a.isalnum())
print('\033[1;32mSomente têm letras maiúsculas? ', a.isupper())
print('\033[1;36mSomente têm letras minúsculas? ', a.islower())
print('\033[1;30mÉ decimal? ', a.isdecimal())
print('\033[1;34mEstá capitulada? ', a.istitle())
