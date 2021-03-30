# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[4;35mOlá, como vai?\033[m')
v = float(input('\nQual o valor da casa? R$'))
s = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))
