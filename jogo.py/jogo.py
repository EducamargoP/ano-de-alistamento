from datetime import date

ano = date.today().year
nome = input('diga seu nome ?')
num = int(input('diga o ano em que nasceu ?'))
idade = ano - num
print("olá {} voce nasceu em {} tem {} idade".format(nome, num , idade))
if idade == 18:
    print('você deve se alistar IMEDIATAMENTE!')
elif idade > 18:
    saldo = idade - 18
    print('você passou do prazo {}'.format(saldo))
    atual = saldo - ano
    print('seu alistamento foi em {}'.format(atual))
elif idade < 18:
    saldo = idade - 18
    atual = saldo + ano
    print('ainda falta {} para o alistamento'.format(saldo))
    print('seu alistamento sera em {} '.format(ano))
