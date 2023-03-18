def descRaca():
    raca = ['Humano', 'Elfo', 'Anao', 'Halfling', 'Draconato', 'Gnomo', 'Meio-Elfo', 'Meio-Orc', 'Tiferino']
    for i in range(len(raca)):
        print(i+1, raca[i])


def descSubClass():
    descSubClass=['2,1 Alto Elfo', '2,2 Elfo Silvestre', '2,3 Drow']
    for i in range(len(descRaca)):
        print(i+1, descRaca[i])
    
num = str(input('escolha uma raca:'))
subRaca = str(input('escolha uma sub raca:'))


if num == '1':
    print("humano: +1 em todos os atributos,")
elif num == '2':
    print("Elfo +2 destreza.")
    print('2,1 Alto Elfo 2,2 Elfo Silvestre 2,3 Drow')    
    if(subRaca == '2,1'):
        print("Alto Elfo adicional de +1 inteligencia.")
    elif(subRaca == '2,2'):
        print("Elfo Silvestre adicional de +1 sabedoria.")
    elif(subRaca == '2,3'):
        print("Drow adicional de +1 de carisma.")
elif num == '3':
    print("Anao +2 costituicao.")
    if(subRaca == '3,1'):
        print("Anao da colina adicional de +1 sabedoria.")
    elif(subRaca == '3,2'):
        print("Anao da montanha adicional de +2 em forca.")
elif num == '4':
    print ("Halfling +2 de destreza.")
    if(subRaca == '4,1'):
        print("Pes-Ligeiros adicional de +1 carisma.")
    elif(subRaca == '4,2'):
        print("Robusto adicional de +1 costituicao.")
elif num == '5':
    print ("Draconato +2 de forca e +1 carisma.")
elif num == '6':
    print ("Gnomo +2 inteligencia.")
    if(subRaca =='6,1'):
        print("Gnomo dos Bosques adicional de +1 destreza.")
    elif(subRaca == '6,2'):
        print("Gnomo das Rochas +1 costituicao.")
elif num == '7':
    print ("Meio-Elfo +2 carisma, +1 destrea e +1 inteligencia.")
elif num == '8':
    print ("Meio-Orc +2 forca e +1 constituicao.")
elif num == '9':
    print ("Tiferino +2 carisma e +1 inteligencia.")
else:
    print("digite 1 2 2,1 2,2 2,3 3 3,1 3,2 4 4,1 4,2 5 6 6,1 6,2 7 8 ou 9 nao",num)
print('--------------------------------------------------------------------------------')


classe = ['Barbaro', 'Bardo', 'Bruxo', 'Clerigo', 'Druida', 'Feiticeiro', 'Guardiao', 'Guerreiro', 'Ladino', 'Mago', 'Monge' ,'Paladino']

for i in range(len(classe)):
    print(i+1, classe[i])

num = str(input('escolha uma classe:'))

if num == '1':
    print("Barbaro")
elif num == '2':
    print("Bardo")
elif num == '3':
    print("Bruxo")
elif num == '4':
    print("Clerigo")
elif num == '5':
    print("Druida")
elif num == '6':
    print("Feiticeiro")
elif num == '7':
    print("Guardiao")
elif num == '8':
    print("Guerreiro")
elif num == '9':
    print("Ladino")
elif num == '10':
    print("Mago")
elif num == '11':
    print("monge")
elif num == '12':
    print("Paladino")
else:
    print("digite 1 2 3 4 5 6 7 8 9 10 11 ou 12 nao",num)
print('--------------------------------------------------------------------------------')


antecedente = ['Acolito', 'Artesao de Guilda', 'Artista', 'Charlatao', 'Criminoso', 'Eremita', 'Forasteiro', 'Heroi do Povo', 'Marinheiro', 'Crianca de Rua', 'Nobre', 'Sabio', 'Soldado']

for i in range(len(antecedente)):
    print(i+1, antecedente[i])

num = str(input('escolha um antecedente:'))

if num == '1':
    print("Acolito")
elif num == '2':
    print("Artesao de Guilda")
elif num == '3':
    print("Artista")
elif num == '4':
    print("Charlatao")
elif num == '5':
    print("Criminoso")
elif num == '6':
    print("Eremita")
elif num == '7':
    print("Forasteiro")
elif num == '8':
    print("Heroi do Povo")
elif num == '9':
    print("Marinheiro")
elif num == '10':
    print("Crianca de Rua")
elif num == '11':
    print("Nobre")
elif num == '12':
    print("Sabio")
elif num == '13':
    print("Soldado")
else:
    print("digite 1 2 3 4 5 6 7 8 9 10 11, 12 ou 13 nao",num)
print('--------------------------------------------------------------------------------')
