from datetime import date


idade = int(input('informe sua idade:'))

sexo = str(input('informe seu sexo M ou F:'))

nome = str(input('informe seu nome:'))

e_mail = str(input('informe seu email:'))

telefone = str(input('informe o telefone:'))

nascimento = str(input('informe data de nascimento:'))

if sexo == 'm' or sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'f' or sexo == 'F':
        sexo = 'Feminino'
else:    
    print('Sexo não informado')

if nome == '':
    print(' nome não informado')
else:
    print('nome salvo')

if e_mail == '':
    print('email não informado')
else:
    print('email salvo')

if telefone == '':
    print('numero de telefone não informado')
else:
    print('numero de telefone salvo')

if nascimento == '':
    print('informe data de nacimento')
else:
    print('data de nascimento salva')

if idade == '':
    print('informe idade')
else:
    print('ok')