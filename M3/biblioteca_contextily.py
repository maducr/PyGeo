import contextily as cx
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados de setores censitários
setores = gpd.read_file('M3/aquivos_aula/35SEE250GC_SIR.shp')

# Filtrando setores para São José dos Campos
setores = setores[setores.NM_MUNICIP == 'SÃO JOSÉ DOS CAMPOS'].reset_index()

# Carregando os dados de população
pop10 = pd.read_csv('M3/aquivos_aula/residentes.csv', sep=';')
pop10.rename(columns={"V001": "pop"}, inplace=True)
pop10 = pop10[['Cod_setor', 'pop']]

# Criando coluna numérica para Cod_setor em setores
setores['Cod_setor'] = pd.to_numeric(setores.CD_GEOCODI)

# Realizando o merge entre setores e população
set_pop = setores.merge(pop10, on="Cod_setor", how='left')

bares = gpd.read_file("M3/aquivos_aula/bares_sjc.shp")
bares = bares.to_crs(crs = "epsg:4674") 

# MAPA 1
fig, eixo = plt.subplots(figsize=(10, 10))

# Plotando os dados da coluna pop usando o mapa de cores seismic
sjc_join = gpd.sjoin(bares.to_crs(crs="epsg:4674"), set_pop, how="inner", predicate="within")
sjc_join.plot(ax=eixo, cmap="seismic", column="pop", markersize=200, scheme="naturalbreaks", k=2, legend=True)

# Definindo os limites dos eixos x e y dos plots
eixo.set_xlim(-45.95, -45.86)
eixo.set_ylim(-23.26, -23.13)

fig.suptitle("População no setor censitário do bar")

# Adicionando o mapa base do provedor OpenStreetMap
cx.add_basemap(ax=eixo, crs="epsg:4674", zoom=13, source=cx.providers.OpenStreetMap.Mapnik)
fig.tight_layout(pad=3)

# MAPA 2
fig, eixo = plt.subplots(figsize=(10, 10))

sjc_join.plot(ax=eixo, cmap="seismic", column="pop", markersize=200, scheme="naturalbreaks", k=2, legend=True)

eixo.set_xlim(-45.95, -45.86)
eixo.set_ylim(-23.26, -23.13)

fig.suptitle("População no setor censitário do bar (mapa 2)")

cx.add_basemap(ax=eixo, crs="epsg:4674", zoom=13)
fig.tight_layout(pad=3)

# MAPA 3
fig, eixo = plt.subplots(figsize=(10, 10))

sjc_join.plot(ax=eixo, cmap="seismic", column="pop", markersize=200, scheme="naturalbreaks", k=2, legend=True)

eixo.set_xlim(-45.95, -45.86)
eixo.set_ylim(-23.26, -23.13)

fig.suptitle("População no setor censitário do bar (mapa 3)")

# Adicionando o mapa base do provedor CartoDB Positron
cx.add_basemap(ax=eixo, crs="epsg:4674", zoom=13, source=cx.providers.CartoDB.Positron)
fig.tight_layout(pad=3)

output_shapefile = 'M3/resultados/mapas/populacao_setor_censitario.shp'
sjc_join.to_file(output_shapefile)

output_png = 'M3/resultados/mapas/populacao_setor_censitario.png'
plt.savefig(output_png, dpi=300, bbox_inches='tight')

plt.show()
