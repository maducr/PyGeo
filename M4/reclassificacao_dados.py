# RECLASSIFICAÇÃO DE DADOS #

import geopandas as gpd
import matplotlib.pyplot as plt

# Carregando os dados
dados = gpd.read_file("M4/arquivos-aula/TravelTimes_to_5975375_RailwayStation.shp")

# Removendo valores -1 (no data) da coluna pt_r_tt
dados_pt_r_tt = dados[dados['pt_r_tt'] >= 0]

# Plotando o mapa para a coluna pt_r_tt
fig, ax = plt.subplots(figsize=(10, 6))
dados_pt_r_tt.plot(
    ax=ax,
    column="pt_r_tt",
    scheme="Fisher_Jenks", # Scheme - indica o tipo de classificador a ser usado (sse classificador vem da biblioteca mapclassify)
    k=9, # K - indica o número de classes e cmap a paleta de cores a ser usada
    cmap="RdYlBu_r",
    linewidth=0,
    legend=True,
    legend_kwds={"bbox_to_anchor": (1.10, 0.82, 0.3, 0.2)}
)

# Salvando o mapa como imagem
plt.savefig("M4/resultados/m4-2/mapa_pt_r_tt.png", bbox_inches="tight")
plt.close()

# Removendo valores -1 (no data) da coluna walk_t
dados_walk_t = dados[dados['walk_t'] >= 0]

# Plotando o mapa para a coluna walk_t
fig, ax = plt.subplots(figsize=(10, 6))
dados_walk_t.plot(
    ax=ax,
    column="walk_t",
    scheme="Fisher_Jenks",
    k=9,
    cmap="RdYlBu_r",
    linewidth=0, # Linewidth - indica a espessura da linha e lengend = True indica que a legenda deve ser mostrada
    legend=True,
    legend_kwds={"bbox_to_anchor": (1.5, 1.01)}
)

# Salvando o mapa como imagem
plt.savefig("M4/resultados/m4-2/mapa_walk_t.png", bbox_inches="tight")
plt.close()