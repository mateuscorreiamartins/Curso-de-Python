# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "A";
# Em que posição ela aparece a primeira vez;
# Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip()
print('A letra A aparece {} vezes. '.format(frase.upper().count('A')))
print('A letra A aparece a primeira vez na posição {}.'.format(frase.upper().find('A') + 1))
print('A letra A aparece a última vez na posição {}.'.format(frase.upper().rfind('A') + 1))
