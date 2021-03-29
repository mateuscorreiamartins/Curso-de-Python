# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e
# R$0,45 para viagens mais longas.

d = float(input('Qual a distância da viagem? '))
if d <= 200:
    v1 = 0.50 * d
    print('O valor da sua passagem é: R${} '.format(v1))
else:
    v2 = 0.45 * d
    print('O valor da sua passagem é: R${} '.format(v2))
