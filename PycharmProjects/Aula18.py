from datetime import date

nome = str(input('qual seu nome: '))

endereco = str(input('qual seu endereço: '))

anoNascmento = str(input('qual sua data de nascimento: '))

# hdata = date.strftime(anoNascmento, '%d/%m/%Y')

dias = date.today()

x = '{}/{}/{}'.format(dias.day,dias.month,dias.year)
print(x)

# x = dias.strftime('%d/%m/%Y')
# print(x)

# idade = anoNascmento - dias.strftime('%Y')

print(anoNascmento, type(anoNascmento))

datanovo = date.strptime(anoNascmento, '%d/%m/%Y').datanovo
