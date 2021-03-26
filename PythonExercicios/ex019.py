# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido é: {}. '.format(escolhido))

# Código que fiz antes de assistir a resolução
nome1 = input('Escreva o nome do primeiro aluno e o número escolhido: ')
nome2 = input('Escreva o nome do segundo aluno e o número escolhido: ')
nome3 = input('Escreva o nome do terceiro aluno e o número escolhido: ')
nome4 = input('Escreva o nome do quarto aluno e o número escolhido: ')
s = random.randint(1,4)
print('O aluno escolhido é o de número: {}.'.format(s))
