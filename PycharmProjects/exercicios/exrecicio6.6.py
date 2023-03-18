valor1a_str = input('informe valor 1a:')
valor1a = float(valor1a_str)

valor2b_str = input('informe valor 2b:')
valor2b = float(valor2b_str)

valor3c_str = input('informe valor 3c:')
valor3c = float(valor3c_str)

mediaPonderada = ((valor1a * 1) + (valor2b * 2) + (valor3c * 3) / (1+2+3))

print ('Média ponderada', mediaPonderada)