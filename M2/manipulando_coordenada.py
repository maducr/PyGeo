# MANIPULANDO FORMAS DE SISTEMAS DE COORDENADAS #
import pandas as pd
import geopandas as gpd

shapefile = "M2/arquivos_aulas/a__031_001_americaDoSul.shp" # Caminho de leitura

bra = gpd.read_file(shapefile)

print(bra.crs) # Verificando o CRS (Coordinade Reference System) do shapefile

print("--------------------------------------------------------------")

print(bra.head()) # Visualizando os atributos do shapefile

print("--------------------------------------------------------------")

print(bra['geometry'].head()) # Visualizando a coluna "geometria"

print("--------------------------------------------------------------")

# CRIANDO CÓPIA DO GEODATAFRAME MODIFICANDO O CRS

bra_wgs84 = bra.to_crs(epsg = 3395)
print(bra_wgs84.crs)

print("--------------------------------------------------------------")

print(bra_wgs84['geometry'].head())

print("--------------------------------------------------------------")

# CRIANDO CÓPIA DO GEODATAFRAME MAS DESSA VEZ UTILIZANDO O CRS
bra_Albers = bra.to_crs(crs = 'esri:102033')
print(bra_Albers.crs)