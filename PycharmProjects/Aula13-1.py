def descRaca():
    raca=["humano","elfo"]
    for i in range(len(descRaca)):
        print(i, descRaca[i])

def descSubRacaElfo():
    subRaca=["zizinho","dark"]

def classe():
    clas=["toto","feijão"]

def menu():
    print("-----------------------------")
    print("BEM VINDO A RPG D&D")
    print("VAMOS MONTAR SEU PERSONAGEM:")
    print("-----------------------------")

def defoult():
    print("valor de fu")

if __name__ == "__main__":
    switch = {
        "1":menu,
        "2":classe
    }

    selRaca = str(input('informe um valor:'))
    case = switch.get(selRaca, defoult)
    case()