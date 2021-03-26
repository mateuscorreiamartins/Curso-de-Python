# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia
# e R$0.15 por Km rodado.

d = int(input('Quantos dias você ficou com o carro? '))
k = float(input('Quantos quilômetros você percorreu com ele? '))
if d == 0:
    print('\033[4;31mDigite um valor válido.\033[m')
else:
    kmr = k * 0.15
    di = d * 60
    print('O preço a pagar é: R$ {:.2f}.'.format(kmr + di))
