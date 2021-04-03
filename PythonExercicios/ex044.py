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
if cond == 1:
    print('\n\033[4;30mO valor de R${} com desconto de 10% fica R${}\033[m'.format(v, v - (10 * v / 100)))
elif cond == 2:
    print('\n\033[4;30mO valor de R${} com desconto de 5% fica R${}\033[m'.format(v, v - (5 * v / 100)))
elif cond == 3:
    print('\n\033[4;30mO valor de R${} deverá ser pago em duas vezes de R${}'.format(v, v / 2))
elif cond == 4:
    vezes = int(input('\033[1;37mEm quantas vezes você vai pagar?\033[m '))
    if vezes < 3:
        print('\033[4;31mEsta opção é para 3 vezes ou mais!\033[m')
    else:
        nvalor = v + (20 * v / 100)
        print('\n\033[4;30mO valor de R${} com 20% de juros fica R${}\n'
            'Esse valor deverá ser pago em {} vezes de R${}'.format(v, nvalor, vezes, nvalor / vezes))
else:
    print('\033[4;31mOPÇÃO INVÁLIDA!\033[m')
