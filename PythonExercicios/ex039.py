# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
sexo = int(input('\n\033[1;30mOlá! Qual o seu sexo?\n\n'
                 '\033[1;34m[ 1 ] MASCULINO\n'
                 '\033[1;36m[ 2 ] FEMININO\n\033[m'
                 '\n\033[1;30mResposta: \033[m'))
