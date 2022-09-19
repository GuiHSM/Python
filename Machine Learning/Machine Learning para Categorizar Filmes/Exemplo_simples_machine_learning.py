# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:08:21 2020

@author: guisa
"""
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.dummy import DummyClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split as tts
import pandas as pd
import seaborn as sns
from datetime import datetime

SEED=20

dados=pd.read_csv("car_prices.csv")
ah_renomear={
        "Unnamed: 0":"codigo",
        "mileage_per_year":"milhas_por_ano",
        "model_year":"ano_do_modelo",
        "price":"preco",
        "sold":"vendido"
        }
dados=dados.rename(columns=ah_renomear)
#print(dados.head())
trocar={
        "yes":1,
        "no":0
        }
ano_atual=datetime.today().year
dados["vendido"]=dados.vendido.map(trocar)
dados["idade_do_modelo"]=2019-dados.ano_do_modelo

dados["km_por_ano"]=1.6094*dados.milhas_por_ano

dados=dados.drop(columns=["codigo","milhas_por_ano","ano_do_modelo"],axis=1)
print(dados.head())

#a=sns.scatterplot(y="preco",x="idade_do_modelo",data=dados,hue=dados["vendido"])

x=dados[["km_por_ano","idade_do_modelo","preco"]]
y=dados["vendido"]

raw_treino_x,raw_teste_x,treino_y,teste_y=tts(x,y,test_size=0.25,stratify=y,random_state=SEED)
scaler=StandardScaler()
scaler.fit(raw_treino_x)
treino_x=scaler.transform(raw_treino_x)
teste_x=scaler.transform(raw_teste_x)

#model=LinearSVC(random_state=SEED)
model=SVC(random_state=SEED)
model.fit(treino_x,treino_y)

previsoes=model.predict(teste_x)
taxa_de_acertos=accuracy_score(teste_y,previsoes)
print("%.2f"%(taxa_de_acertos*100))
'''
dummy=DummyClassifier(random_state=SEED)

dummy=DummyClassifier(random_state=SEED,strategy="most_frequent")
dummy.fit(treino_x,treino_y)
taxa_de_acertos=dummy.score(teste_x,teste_y)
print("%.2f"%(taxa_de_acertos*100))
'''