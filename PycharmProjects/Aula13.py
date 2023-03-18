def function():
    print("case 1 selecionado")

def function2():
    print("case 1 selecionado")

def defould():
    print("valor de fu")

if __name__ == "__main__":
    switch = {
        "1":function,
        "2":function2
    }

case = switch.get("1", defould)
case()