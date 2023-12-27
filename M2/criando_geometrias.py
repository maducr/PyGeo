# SHAPEFILE DO ZERO #
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from matplotlib.ticker import FuncFormatter

# Criando um GeoDataFrame vario
dados_nov = gpd.GeoDataFrame()

# Criando uma coluna vazia para armazenar as geometrias
dados_nov["geometry"] = None

# Lista com pares (tuplas) das coordenadas referentes a geometria escolhida (nesse caso o Parque Trianon em SP)
coordenadas = [
    (-23.5615974,-46.6573198),
    (-23.5626145,-46.6583302),
    (-23.5635077,-46.6572431),
    (-23.5635077,-46.6572431),
    (-23.5635077,-46.6572431),
    (-23.5624905,-46.6559936)
]

# Criando o polígono a partir da lista
trianon_plg = Polygon(coordenadas)

print(type(trianon_plg)) # Visualizando o tipo de dado da variável criada

print("------------------------------------------------------------------------------------------------------------------------")

print(trianon_plg) # Visualizando a estrutura dos dados

# Adicionando o polígono ao GeoDataFrame
dados_nov.loc[0, "geometry"] = trianon_plg

# PLOTAGEM

# Cria a figura e os eixos para plotagem (tamanho 10x10 polegadas)
fig, ax = plt.subplots(figsize=(10, 10))

# Plotagem
dados_nov.plot(ax = ax, color = '#426F42')

# Nomeando os eixos y e x
ax.set_ylabel("EIXO NORTE-SUL")
ax.set_xlabel("EIXO OESTE-LESTE")

# Rotacionando os rótulos numéricos do eixo y
plt.yticks(rotation=90)

# Formatando os rótulos dos eixos x e y com duas casas decimais
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:.2f}'.format(x)))
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))

# Exibindo o gráfico
#plt.show()

print("------------------------------------------------------------------------------------------------------------------------")

# INSERINDO A GEOMETRIA CRIADA NO GEODATAFRAME VAZIO

dados_nov.loc [0,"geometry"] = trianon_plg # "loc" vem de localiza (nesse caso localizar a linha da índice 0 e a coluna geometry)

dados_nov.loc[0, "Lugar"] = "Trianon" # criando uma coluna para armazenar o nome da geometria

print(dados_nov)

print("------------------------------------------------------------------------------------------------------------------------")

# MANIPILANDO SISTEMAS DE COORDENADAS

# Definindo a projeção
dados_nov = dados_nov.set_crs("epsg:3857")

print(dados_nov.crs)

# EXPORTANDO O SHAPEFILE

# Caminho de saída
shapefile = "M2/salvando-shp-resultados/m2.3/trianon_pseudomercartor.shp"

dados_nov.to_file(shapefile) # Exportando