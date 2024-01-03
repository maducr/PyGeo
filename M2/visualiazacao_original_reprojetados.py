import geopandas as gpd
import matplotlib.pyplot as plt
from pyproj import CRS

# Caminho do shapefile
shapefile_path = "M2/arquivos_aulas/a__031_001_americaDoSul.shp"
bra = gpd.read_file(shapefile_path)

# Define as projeções
sc_geo = CRS('EPSG:4326')  # Geográfica
sc_albers = CRS('esri:102033')  # Albers Equal Area Conic
sc_mercator = CRS('EPSG:3395')  # Mercator
sc_br_albers = CRS('+proj=cea +lon_0=0 +lat_ts=45 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs')  # Brasil Albers
sc_gall_peters = CRS('+proj=cea +lon_0=0 +lat_ts=45 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs')  # Gall-Peters
sc_stereographic = CRS('+proj=stere +lat_0=-90 +lat_ts=-90 +lon_0=-63 +k=1 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs')  # Estereográfica polar

# Reprojeta os dados
bra_geo = bra.to_crs(crs=sc_geo)
bra_albers = bra.to_crs(crs=sc_albers)
bra_mercator = bra.to_crs(crs=sc_mercator)
bra_br_albers = bra.to_crs(crs=sc_br_albers)
bra_gall_peters = bra.to_crs(crs=sc_gall_peters)
bra_stereographic = bra.to_crs(crs=sc_stereographic)

# Configura a figura e os subplots
fig, ax = plt.subplots(2, 3, figsize=(15, 10))

# Plotagem dos mapas
bra_geo.plot(facecolor="gray", ax=ax[0, 0])
ax[0, 0].set_title("SIRGAS 200 - Geográfica")

bra_albers.plot(facecolor="gray", ax=ax[0, 1])
ax[0, 1].set_title("Albers - Projetada")

bra_mercator.plot(facecolor="gray", ax=ax[1, 0])
ax[1, 0].set_title("Mercator - Projetada")

bra_br_albers.plot(facecolor="gray", ax=ax[1, 1])
ax[1, 1].set_title("Brasil Albers - Projetada")

bra_gall_peters.plot(facecolor="gray", ax=ax[0, 2])
ax[0, 2].set_title("Gall-Peters - Projetada")

bra_stereographic.plot(facecolor="gray", ax=ax[1, 2])
ax[1, 2].set_title("Estereográfica polar - Projetada")

plt.tight_layout()  # Remove espaços ou sobreposições entre plots

plt.show()

print("--------------------------------------------------------------")

# Calculando a área do Brasil para cada um dos CRS
print("Estereografica conforme:", bra_stereographic[bra_stereographic.NAME_SORT=="Brazil"].to_crs(crs=sc_geo).area/1000000)
print("Gall-Peters equivalente:", bra_gall_peters[bra_gall_peters.NAME_SORT=="Brazil"].to_crs(crs=sc_geo).area/1000000)
print("Albers equivalente:", bra_albers[bra_albers.NAME_SORT=="Brazil"].to_crs(crs=sc_geo).area/1000000)
print("Brasil Albers equivalente:", bra_br_albers[bra_br_albers.NAME_SORT=="Brazil"].to_crs(crs=sc_geo).area/1000000)
print("SIRGAS 2000:", bra_geo[bra_geo.NAME_SORT=="Brazil"].area/1000000)
print("WGS84:", bra.to_crs(crs=sc_geo).area/1000000)