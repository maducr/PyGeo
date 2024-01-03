# BIBLIOTECA OSMNX E DADOS DO OPEN STREET MAPS NO PYTHON #
import osmnx as ox
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

lugar = "Vila Ema, São José dos Campos" # Local para o qual se quer obter as informações do OSM

rede = ox.graph_from_place(lugar) # Extraindo a rede de ruas com base no nome da localização

# print(type(rede)) = <class 'networkx.classes.multidigraph.MultiDiGraph'> -> Multidigrafo - forma de representação de arruamentos/redes por arestas e nós

fig, ax = ox.plot_graph(rede, show=False, close=False)  # Plotagem

# Adicionando linhas brancas para as arestas (ruas)
for edge in rede.edges():
    edge_nodes = list(edge)
    coordinates = [(rede.nodes[node]['x'], rede.nodes[node]['y']) for node in edge_nodes]
    x, y = zip(*coordinates)
    ax.plot(x, y, color='white', linewidth=1, alpha=0.7, zorder=1)  # Ajuste a transparência aqui

# Adicionando círculos brancos para os nós (vértices)
for node, data in rede.nodes(data=True):
    x, y = data['x'], data['y']
    ax.scatter(x, y, color='white', edgecolors='black', s=50, zorder=2)

plt.axis('off')  # Desativar os eixos

output_png = 'M4/resultados/linhas_circulo.png'
plt.savefig(output_png, dpi=300, bbox_inches='tight', transparent=True)

# CRIANDO POLÍGONO
area = ox.geocode_to_gdf(lugar)

area.plot() # Plotagem

output_area = 'M4/resultados/area.png'
plt.savefig(output_area, dpi=300, bbox_inches='tight')

# POLÍGONOS DE PRÉDIOS
predios = ox.geometries_from_place(lugar, tags = {"building":True})
print(type(predios))

predios.plot()

output_predios = 'M4/resultados/predios.png'
plt.savefig(output_predios, dpi=300, bbox_inches='tight')

# POLÍGONOS DE ÁRVORES
arvores = ox.geometries_from_place(lugar, tags={"natural":"tree"})

arvores.plot()

output_arvores = 'M4/resultados/arvores.png'
plt.savefig(output_arvores, dpi=300, bbox_inches='tight')

nos,arestas= ox.graph_to_gdfs(rede) # Extraindo e separando nós e arestas em dois geodataframes

nos.plot()
arestas.plot()

output_nos = 'M4/resultados/nos.png'
plt.savefig(output_nos, dpi=300, bbox_inches='tight')

output_arestas = 'M4/resultados/arestas.png'
plt.savefig(output_arestas, dpi=300, bbox_inches='tight')

# Verificando os preimeiros registros 
print(predios.head())
print("--------------------------------------------------------------")
print(nos.head())
print("--------------------------------------------------------------")
print(arestas.head())
print("--------------------------------------------------------------")
 
# BIBLIOTECA PARA VERIFICAR OS VALORES ÚNICOS DO TIPO DE PRÉDIO
print(pd.unique(predios.building))
print("--------------------------------------------------------------------")

# Obter o nome de todas as colunas
print(predios.columns)
("--------------------------------------------------------------------")