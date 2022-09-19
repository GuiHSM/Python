# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:27:05 2020

@author: guisa
"""

import numpy as np
import pandas as pd
dataset=pd.read_csv("db.csv",sep = ";",index_col=0)
pd.set_option("display.max_rows",10)
#pd.set_option("display.max_columns",1000)
#print(dataset.dtypes)
#print(dataset[["Quilometragem","Valor"]].describe())
batata=[500,10]
queijo=[500,10]
for item in zip(batata,queijo):
    print(item)
outro=["a","b"]
dicionario=dict(zip(outro,batata))
dicionario["c"]=400
del dicionario["a"]
"a" in dicionario
def bata(a,b,c):
    return a+b+c
def q(lista):
    return sum(lista)/len(lista)
print(q(dicionario.values()))
nomes=["afonso","josé","rodrigo"]
dicto=[{"Nome":"afonso","renda":108},{"Nome":"josé","renda":158},{"Nome":"rodrigo","renda":198}]
serie=pd.Series(nomes)
data=pd.DataFrame(dicto)
data["Nome"]
data.iloc[1:2]
#queries
select = data.Nome=="rodrigo"
dataset.Quilometragem.isna()
dataset.fillna(0,inplace=True)
dataset.dropna(subset=['Quilometragem'],inplace=True)
dataset.to_csv("db_novo.csv")