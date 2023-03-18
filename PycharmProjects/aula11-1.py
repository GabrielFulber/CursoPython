def func1():
    print("case 1")

def func2():
    print("case 2")

def defoult():
    print("default")

def swith(case):
    if case == "1":
        return func1
    elif case =="2":
        return func2
    else:
        return defoult

if __name__ == "__main__":
    switch = {
        "1": func1,
        "2": func2
    }
    num = str(input('informe 1 ou 2 :'))

    case = switch.get(num, defoult)
    case()