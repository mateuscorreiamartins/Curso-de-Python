# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

n = float(input('Digite o preço do produto: R$'))
p = (5 / 100) * n
print('O valor do produto com o desconto de 5% é de: {}.'.format(n - p))
