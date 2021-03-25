# Escreva um programa que converta uma 
# temperatura digitada em ºC e converta para ºF.

t = float(input('Digite a temperatura para que eu faça a conversão: '))
c = t * 1.8 + 32
print('A temperatura em ºFahrenheit é: {:.2f}.'.format(c))
