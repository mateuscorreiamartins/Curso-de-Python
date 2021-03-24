# Escreva um programa que leia um valor em 
# metros e o exiba convertido em centímetros e milímetros.

v = float(input('Digite o valor em metros: '))
c = v * 100
m = v * 1000
print('O valor em centímetros é: {}cm. \nO valor em milímetros é: {}mm.'.format(c, m))
