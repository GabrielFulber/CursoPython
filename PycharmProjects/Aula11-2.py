raca = ['humano', 'Elfo', 'Anao']

for i in range(len(raca)):
    print(i+1, raca[i])

num = str(input('escolha uma raca:'))

if num == '1':
    print("humano: +1 em todos os atributos")
elif num == '2':
    print("Elfo +1 des +1car")
elif num == '3':
    print("Anao +1f +1const")
else:
    print("sua mula eu falei 1, 2 ou 3 eu nao falei",num)
