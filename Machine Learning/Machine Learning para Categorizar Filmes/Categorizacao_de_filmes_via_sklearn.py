#inercia é o erro quadrático médio, algo como a variância em relação ao centróide mais próximo

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from scipy.cluster.hierarchy import dendrogram,linkage
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(20)

filmes=pd.read_csv("movies.csv")
ah_renomear={
	"title":"titulo",
	"genres":"generos"
}
filmes=filmes.rename(columns=ah_renomear)
generos=filmes.generos.str.get_dummies()
dados_filmes=pd.concat([filmes,generos],axis=1)

scaler = StandardScaler()
generos_escalados=scaler.fit_transform(generos)
modelo=KMeans(n_clusters=17)
modelo.fit(generos_escalados)

'''
#visualizando com graficos de barras o agrupamento do Kmeans
grupos=pd.DataFrame(modelo.cluster_centers_,columns=generos.columns)
plot=grupos.transpose().plot.bar(subplots=True,figsize=(50,50),sharex=False,rot=0)
plot[0].get_figure().savefig("bar.png")
#grupo=0
#filtro=modelo.labels_== grupo
#print(dados_filmes[filtro].sample(10))
'''
'''
#Visualizando o agrupamento do Kmeans em um scatterplot
tsne=TSNE()
visualizacao=tsne.fit_transform(generos_escalados)
sns.set(rc={"figure.figsize":(13,13)})
sns.scatterplot(x=visualizacao[: ,0],y=visualizacao[: ,1],hue=modelo.labels_,palette=sns.color_palette("Set1",17)).get_figure().savefig("scatter.png")
'''
'''
#elbow method, cria o gráfico e vê oponto de "quebra", derivada=0
def kmeans(n_clusters,generos):
    modelo=KMeans(n_clusters=n_clusters)
    modelo.fit(generos)
    return [n_clusters,modelo.inertia_]
resultado= [kmeans(i,generos_escalados) for i in range(1,41)]
resultado=pd.DataFrame(resultado,columns=["n_grupos","inertia"])
resultado.inertia.plot(xticks=resultado.n_grupos,figsize=(20,20)).get_figure().savefig("elbow.png")
#Deu 17
'''
##visualizando os dados como dendograma
grupos=pd.DataFrame(modelo.cluster_centers_,columns=generos.columns)
matriz_distancia=linkage(grupos)
dendrogram(matriz_distancia)
plt.gcf()
plt.savefig("dendrogram.png")
