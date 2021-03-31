# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n1 = float(input('Qual a sua primeira nota? '))
n2 = float(input('Qual a sua segunda nota? '))
m = (n1 + n2) / 2
if m < 5:
    print('\033[4;31mVocê está REPROVADO!\033[m')
elif 5 < m <= 6.9:
    print('\033[4;33mVocê está de RECUPERAÇÃO!\033[m')
elif m > 7:
    print('\033[4;36mVocê está APROVADO!\033[m')
