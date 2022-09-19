# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:56:02 2020

@author: guisa
"""
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import pandas as pd
dados, _ = make_blobs(n_samples=1000, n_features=2)
dados = pd.DataFrame(dados, columns=['coluna1', 'coluna2'])
dados.head()

plt.scatter(x=dados.coluna1, y=dados.coluna2)

modelo = KMeans(n_clusters=3)
grupos = modelo.fit_predict(dados)
plt.scatter(x=dados.coluna1, y=dados.coluna2, 
            c=grupos,
           cmap='viridis')
centroides = modelo.cluster_centers_
plt.scatter(dados.coluna1, dados.coluna2,
            c=grupos,
           cmap='viridis')
plt.scatter(centroides[:, 0], centroides[:, 1],
           marker='X', s=169, linewidths=5,
           color='g', zorder=8)