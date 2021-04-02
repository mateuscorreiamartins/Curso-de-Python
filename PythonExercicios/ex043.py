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
if imc < 18.5:
    print('\033[4;31mVocê está abaixo do peso!\033[m ')
elif imc >= 18.5 and imc < 25:
    print('\033[4;36mVocê está no peso ideal! Parabéns!\033[m')
elif imc >= 25 and imc < 30:
    print('\033[1;32mVocê está com sobrepeso!\033[m')
elif imc >= 30 and imc < 40:
    print('\033[4;33mVocê está obeso!\033[m')
elif imc > 40:
    print('\033[4;31mVocê está com obesidade mórbida!\033[m')
