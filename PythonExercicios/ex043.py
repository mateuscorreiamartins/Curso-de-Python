# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

altura = float(input('Qual é a sua altura em metros? '))
peso = float(input('Qual é o seu peso em Kgs? '))
imc = peso / (altura ** 2)
print('\033[1;30mSeu IMC é \033[m{:.2f}'.format(imc))
