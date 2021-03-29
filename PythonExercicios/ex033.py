# Faça um programa que leia três números e mostre qual é o maior
# e qual é o menor.

n1 = int(input('Qual o número? '))
n2 = int(input('Qual o número? '))
n3 = int(input('Qual o número? '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('\033[1;31mO menor número é {}.'.format(menor))
print('\033[1;36mO maior número é {}.'.format(maior))
