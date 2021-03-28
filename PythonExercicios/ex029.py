# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado.

# A multa vai custar R$ 7.00 por cada Km acima do limite.

v = float(input('Qual a velocidade do seu carro? '))
if v > 80:
    m = (v - 80) * 7
    print('Você foi mutado! O valor da sua multa é R${:.2f}. '.format(m))
print('Tenha um bom dia e dirija com segurança! ')
