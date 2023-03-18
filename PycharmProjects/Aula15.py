import pandas as pd
import re as re
import matplotlib.pyplot as plt

df = pd.read_csv("D:/Desktop/leitor/nome.txt")

df_excel = pd.read_excel("D:/Desktop/leitor/nome.xlsx")

df_excel1 = pd.read_excel("D:/Desktop/leitor/Juste.xlsx")

print(df_excel1)
print("---------------------")

print(df)
print("---------------------")
print(df_excel)
print("---------------------")
df_nome = df_excel['nome']

print(df_nome)
print("---------------------")

me_null = df_excel["nome"].replace(to_replace=('M'),value='-',regex=True)

print(me_null)