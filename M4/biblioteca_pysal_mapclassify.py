# RECLASSIFICAÇÃO DE DADOS #
import geopandas as gpd
import matplotlib.pyplot as plt

dados=gpd.read_file("M4/arquivos-aula/TravelTimes_to_5975375_RailwayStation.shp")

dados=dados[dados['pt_r_tt']>=0] # Removendo valores -1 (no data) da coluna pt_r_tt

dados.plot(
    column="pt_r_tt", 
    scheme="Fisher_Jenks", # O argumento scheme indica o tipo de classificador a ser usado. Esse classificador vem da biblioteca mapclassify. 
    k=9, # K indica o número de classes e cmap a paleta de cores a ser usada
    cmap="RdYlBu_r", 
    linewidth=0, 
    legend=True, 
    legend_kwds={"bbox_to_anchor": (1.10,0.82,0.3,0.2)}
) 

dados=dados[dados['walk_t']>=0] # Removendo valores -1 (no data) da coluna walk_t

dados.plot(
    column="walk_t",
    scheme="Fisher_Jenks", 
    k=9, 
    cmap="RdYlBu_r", 
    linewidth=0, # Linewidth indica a espessura da linha e lengend = True indica que a legenda deve ser mostrada
    legend=True, 
    legend_kwds={"bbox_to_anchor":(1.5,1.01)}
)

plt.tight_layout()

plt.show()