# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

r1 = int(input('\nQual a medida da primeira reta? '))
r2 = int(input('Qual a medida da segunda reta? '))
r3 = int(input('Qual a medida da terceira reta? '))
if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r3:
    print('\n\033[1;37mIsso é um triângulo! Agora vou calcular para saber qual é o tipo dele. \n')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Este é um triângulo \033[4;36mEQUILÁTERO\033[m!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Este é um triângulo \033[4;36mISÓSCELES\033[m!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Este é um triângulo \033[4;36mESCALENO\033[m!')
else:
    print('\033[4;31mIsso não é um triângulo.\033[m')
