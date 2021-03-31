# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
sexo = int(input('\n\033[1;30mOlá! Qual o seu sexo?\n\n'
                 '\033[1;34m[ 1 ] MASCULINO\n'
                 '\033[1;36m[ 2 ] FEMININO\n\033[m'
                 '\n\033[1;30mResposta: \033[m'))
if sexo == 2:
    print('\033[1;31mEste programa não foi feito para você!\033[m ')
else:
    ano = int(input('\n\033[1;30mEstou feliz em ter você aqui! Qual o seu ano de nascimento? \033[m'))
    idade = atual - ano
    print('\n\033[4;35mQue bom! Você tem ou vai fazer {} anos.\033[m '.format(idade))
    if idade < 18:
        a1 = 18 - idade
        print('\n\033[1;33mFique tranquilo, pois ainda não é hora de se alistar! '
              'Ainda faltam {} anos.\033[m '.format(a1))
        print('\033[1;34mVocê deverá se alistar no ano de\033[m \033[1;36m{}.\033[m'.format(atual + a1))
    elif idade == 18:
        print('\n\033[4;30mOlha que bacana! Esse é o ano do seu alistamento!\n'
              'Busque a Junta Militar da sua cidade para realizar todos os procedimentos.\033[m')
    else:
        a2 = idade - 18
        print('\n\033[4;31mVocê JÁ PASSOU da idade de se alistar! Passou {} ano(s) da data! '
              '\nSe ainda não se alistou, CORRA ATRÁS DO PREJUÍZO!\033[m'.format(a2))
        print('\033[1;33mVocê deveria ter se alistado no ano de \033[1;31m{}.\033[m'.format(atual - a2))
