# Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu preço normal
# e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS TEUZIN '))
v = float(input('Qual é o valor do produto? R$'))
cond = int(input('''\033[1;34m[ 1 ] À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO.\033[m
\033[1;33m[ 2 ] À VISTA NO CARTÃO: 5% DE DESCONTO.\033[m
\033[1;35m[ 3 ] EM ATÉ 2x NO CARTÃO: PREÇO NORMAL.\033[m
\033[1;32m[ 4 ] 3x OU MAIS NO CARTÃO: 20% DE JUROS.\033[m\n'''))
