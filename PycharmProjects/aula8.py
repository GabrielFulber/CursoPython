idade = int(input('informe sua idade:'))

sexo = str(input('informe o sexo M ou F:'))

if sexo=='m':
    sexo= 'M'
    sexoC= 'MASCULINO'
elif sexo=='f':
    sexo='F'
    sexoC= 'FEMININO'
#validação
if idade>=18 and (sexo=='M'or sexo=='m'):
    print("voce entrou no exercito")

elif idade<18:
    print('sua idade não é valida, você ainda tem', idade, 'anos')
elif sexo=='F':
    print('Seu sexo não é validoseu sexo é',sexoC)    
else:
    print("Informaçao errada, verifique o sexo e idade")

#if idade>= 18 :
#    if sexo =='M':
#        print('pode entrar no exercito')
#    elif sexo == 'm':
#        print('pode entrar no exercito')
#else:
#    print('não pode entrar no exercito')

