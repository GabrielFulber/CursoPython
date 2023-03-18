from multiprocessing.sharedctypes import Value
from os import execl
import pandas as pd
import re as re
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import unicodedata

from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.utils.dataframe import dataframe_to_rows

df_excel = pd.read_excel("D:/Desktop/leitor/Juste.xlsx")

# print(df_excel)
# print("---------------------")

dado_inep_antigo = df_excel[['id_cidade','desc_cidade_1','id_estado_1','inep_1']] 

dado_inep_novo = df_excel[['desc_cidade_2','id_estado_2','inep_2']]

# print(dado_inep_antigo)

# print(dado_inep_novo)


#print(dado_inep_antigo.dtypes)

#print(dado_inep_novo.dtypes)

dado_inep_antigo['id_estado_1']=dado_inep_antigo['id_estado_1'].astype(object)
dado_inep_novo['id_estado_2']=dado_inep_novo['id_estado_2'].astype(object)

#print(dado_inep_antigo.dtypes)

#print(dado_inep_novo.dtypes)

dado_inep_antigo['novo_cidade_1']=dado_inep_antigo['desc_cidade_1'].replace(to_replace=('a','á','à','ã','â','Á','À','Ã','Â'), value = 'A', regex = True)


dado_inep_antigo['novo_cidade_2']=dado_inep_antigo['novo_cidade_1'].replace(to_replace=('e','é','è','ê','É','È','Ê'), value = 'E', regex = True)


dado_inep_antigo['novo_cidade_3']=dado_inep_antigo['novo_cidade_2'].replace(to_replace=('i','í','ì','î','Í','Ì','Î'), value = 'I', regex = True)


dado_inep_antigo['novo_cidade_4']= dado_inep_antigo['novo_cidade_3'].replace(to_replace=('o','ó','ò','õ','ô','Ó','Ò','Õ','Ô'), value = 'O', regex = True)


dado_inep_antigo['novo_cidade_5']=dado_inep_antigo['novo_cidade_4'].replace(to_replace=('u','ú','ù','û','Ú','Ù','Û'), value = 'U', regex = True)


dado_inep_antigo['novo_cidade_6']=dado_inep_antigo['novo_cidade_5'].replace(to_replace=(' '), value = '', regex = True)


dado_inep_novo['novo_cidade_1']=dado_inep_novo['desc_cidade_2'].replace(to_replace=('a','á','à','ã','â','Á','À','Ã','Â'), value = 'A', regex = True)


dado_inep_novo['novo_cidade_2']=dado_inep_novo['novo_cidade_1'].replace(to_replace=('e','é','è','ê','É','È','Ê'), value = 'E', regex = True)


dado_inep_novo['novo_cidade_3']=dado_inep_novo['novo_cidade_2'].replace(to_replace=('i','í','ì','î','Í','Ì','Î'), value = 'I', regex = True)


dado_inep_novo['novo_cidade_4']=dado_inep_novo['novo_cidade_3'].replace(to_replace=('o','ó','ò','õ','ô','Ó','Ò','Õ','Ô'), value= 'O', regex = True)


dado_inep_novo['novo_cidade_5']=dado_inep_novo['novo_cidade_4'].replace(to_replace=('u','ú','ù','û','Ú','Ù','Û'), value = 'U', regex = True)


dado_inep_novo['novo_cidade_6']=dado_inep_novo['novo_cidade_5'].replace(to_replace=(' '), value = '', regex = True)

print(dado_inep_antigo)

# print(dado_inep_novo)
# RELACIONADO A TABELA UM ##
dado_inep_antigo_cid1 = dado_inep_antigo['novo_cidade_6']
dado_inep_antigo1 = dado_inep_antigo[['id_cidade','novo_cidade_6','inep_1']]

# RELACIONADO A TABELA DOIS#
dado_inep_novo_cid2 = dado_inep_novo['novo_cidade_6']
dado_inep_novo2 = dado_inep_novo[['novo_cidade_6','inep_2','id_estado_2']]

# print("---------------------")

# print(dado_inep_antigo1)

# print("---------------------")

# print(dado_inep_novo2)

# dado_inep_antigo1.columns

dado_inep_antigo1.columns = ['id_cidade','novo_cidade','inep']

dado_inep_novo2.columns = ['novo_cidade','inep','id_estado']

# print(dado_inep_antigo1)

# print(dado_inep_novo2)

pd.merge(dado_inep_antigo1, dado_inep_novo2, on=['novo_cidade'])

variavel1 = pd.merge(dado_inep_antigo1, dado_inep_novo2, on=['novo_cidade'])

# print(variavel1)

variavel1.drop_duplicates(subset=['inep_y'])

valores = variavel1.sort_values('id_estado')

# print(valores)

novaplanilha = valores[['id_cidade','novo_cidade','inep_y','id_estado']]

print(novaplanilha)

novaplanilha.columns = ['id_cidade','novo_cidade','inep','id_estado']
x = dado_inep_antigo['desc_cidade_1']

# y = pd.merge(novaplanilha, x,on=[])

novaplanilha.to_excel('teste1.xlsx')