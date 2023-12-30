import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# Shapefile com os dados de setores censitários
setores = gpd.read_file('M3/aquivos_aula/35SEE250GC_SIR.shp')
# print(pd.unique(setores.NM_MUNICIP)) # Mostrando os valores únicos na coluna NM_MUNICIP

# Filtrando setores para São José dos Campos
setores = setores[setores.NM_MUNICIP == 'SÃO JOSÉ DOS CAMPOS']
setores = setores.reset_index() # Resetando o índice das geometrias

# Mostrando o número de linhas e colunas no GeoDataFrame setores
print(setores.shape)
print("--------------------------------------------------------------")

# Primeiros registros do GeoDataFrame
print(setores.head())
print("--------------------------------------------------------------")

# Plotando o GeoDataFrame
fig, ax = plt.subplots()
setores.plot(ax=ax)

setores.to_file('M3/resultados/cocatenacao/mapa_setores_sjc.shp')

plt.savefig('M3/resultados/cocatenacao/mapa_setores_sjc.png')

# plt.show()

# IMPORTANDO A TABELA DE DADOS DO CENSO 2010
pop10 = pd.read_csv('M3/aquivos_aula/residentes.csv', sep = ";")
print(pop10.head())
print("--------------------------------------------------------------")

pop10.rename(columns={"V001":"pop"}, inplace=True) # Renomeando a coluna V001 como pop. Inplace=True indica que alteração deve ser feita na tabela original.
print(pop10.head())
print("--------------------------------------------------------------")

pop10 = pop10[['Cod_setor','pop']] # Selecionando apenas as colunas Cod_setor e pop
print(pop10.head())
print("--------------------------------------------------------------")

print(pop10.shape) # Verificando o número de linhas e colunas da tabela pop10
print("--------------------------------------------------------------")

print(pop10.columns) # Verificando o nome das colunas da tabela pop10
print("--------------------------------------------------------------")

print(type(pop10.Cod_setor[0])) # Checando o tipo de dados da primeira linha da coluna Cod_setor
print("--------------------------------------------------------------")

print(type(setores.CD_GEOCODI[0])) # Checando o tipo de dados da primeira linha da coluna CD_GEOCODI
print("--------------------------------------------------------------")

setores['Cod_setor'] = pd.to_numeric(setores.CD_GEOCODI) # Criando uma nova coluna com os dados da coluna CD_GEOCODI em formato numérico

print(type(pop10.Cod_setor[0])) # Checando o tipo de dados da primeira linha da coluna Cod_setor da tabela pop10
print("--------------------------------------------------------------")

print(type(setores.Cod_setor[0])) # Checando o tipo de dados da primeira linha da coluna Cod_setor da tabela setores
print("--------------------------------------------------------------")

set_pop = setores.merge(pop10, on="Cod_setor", how='left') # Realizando o table join com base na coluna Cod_setor

# Plote os dados de população dos setores censitários
set_pop.plot(column = "pop",cmap = "viridis", vmin = min(set_pop['pop']), vmax = max(set_pop['pop']), missing_kwds = dict(color = "lightgrey",))

set_pop = set_pop[['pop','geometry','Cod_setor']] # Selecionando algumas das colunas  da tabela set_pop

print(setores.shape) # Checando o número de linhas e colunas do geodataframe setores
print("--------------------------------------------------------------")

print(set_pop.shape) # Checando o número de linhas e colunas do geodataframe set_pop
print("--------------------------------------------------------------")
print("--------------------------------------------------------------")

set_pop.to_file('M3/resultados/cocatenacao/pop_sjc.shp')# Exportando o geodataframe set_pop como shapefile

plt.savefig('M3/resultados/cocatenacao/pop_sjc.png')
# plt.show()

# MAPAS BASES #

bares = gpd.read_file("M3/aquivos_aula/bares_sjc.shp")

bares.crs == set_pop.crs # Verificando se os sistemas de coordenadas dos geodataframes bares e set_pop são iguais

# Verifique o sistemas de coordenadas de cada geodataframe
print(bares.crs)
print("--------------------------------------------------------------")

print(set_pop.crs)
print("--------------------------------------------------------------")

bares = bares.to_crs(crs = "epsg:4674") # Reprojetando o geodataframe bares para SIRGAS2000

print(bares.crs == set_pop.crs) # Verificando se os sistemas de coordenadas dos geodataframes bares e set_pop são iguais agora
print("--------------------------------------------------------------")

sjc_join = gpd.sjoin(bares, set_pop,nhow = "inner", predicate = "within")
