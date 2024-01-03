# MAPA COMPLETO - M4.1 #
import osmnx as ox
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

lugar = "Vila Ema, São José dos Campos"

rede = ox.graph_from_place(lugar)
area = ox.geocode_to_gdf(lugar)
nos,arestas = ox.graph_to_gdfs(rede)
predios = ox.geometries_from_place(lugar, tags = {"building":True})
arvores = ox.geometries_from_place(lugar, tags={"natural":"tree"})

# Crie a figura e o eixo de plotagem. E defina o tamanho da figura
fig, eixo= plt.subplots(figsize=(10,10))

# Plote cada um dos geodataframes no eixo de plotagem para garantir que estejam todos na mesma figura 
area.plot(ax=eixo,facecolor="black")
arestas.plot(ax=eixo, linewidth=1, edgecolor="#BC8F8F")
predios.plot(ax=eixo,facecolor="khaki", alpha=0.7)
arvores.plot(ax=eixo, facecolor="green")

geo_dataframes = [area, nos, arestas, predios, arvores]
combined_gdf = gpd.GeoDataFrame(pd.concat(geo_dataframes, ignore_index=True), crs=area.crs)

combined_gdf.to_file('M4/resultados/mapa-completo/mapa.shp')

mapa_completo = 'M4/resultados/mapa-completo/mapa.png'
plt.savefig(mapa_completo, dpi=300, bbox_inches='tight')

print(predios.shape)
print("--------------------------------------------------------------------")
