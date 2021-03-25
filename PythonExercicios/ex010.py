# Crie um programa que leia quanto dinheiro uma pessoa 
# tem na carteira e mostre quantos Dólares ela
# pode comprar.
# Considere US$ 1.00 = R$ 3.27

d = float(input('Digite quanto tem na carteira: '))
print('Você pode comprar US${:.2f} doláres.'.format(d/3.27))
