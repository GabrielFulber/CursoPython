raca = ['Humano', 'Elfo', 'Anão']
#i=1
for i in range(len(raca)):
    print(i, raca[i])

for n in range(5):
    print('-----')
    print('valor de n=',n)
    print('-----')
    for x in range(n):
        if x/2 ==1:
            print('valor par')
            break
        print('valor de x=',x)
