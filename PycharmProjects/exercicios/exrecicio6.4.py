valorPrincipal = 3

valor1_str = input('informe valor a:')
valor1 = float(valor1_str)

valor2_str = input('informe valor b:')
valor2 = float(valor2_str)

valor3_str = input('informe valor c:')
valor3 = float(valor3_str)

mediaHarmonica = valorPrincipal / ((1 / valor1) + (1 / valor2) + (1 / valor3))

print('Média harmônica é: ', mediaHarmonica)