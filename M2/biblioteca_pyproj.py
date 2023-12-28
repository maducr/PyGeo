# CRIANDO CRS #
import pandas as pd
import geopandas as gpd

shapefile = "M2/arquivos_aulas/a__031_001_americaDoSul.shp" # Leitura
bra = gpd.read_file(shapefile)

from pyproj import CRS # Importando os objetos CRS baseado no texto pyproj

# Caso não queria utilizar um CRS não catalogado, ou que não está sendo encontrado, pode-se criar um CRS com base no texto PROJ ou no WKT "https://spatialreference.org/ref/sr-org/brazil-albers-equal-area-conic-wgs84/"

# Crando um objeto CRS baseado no texto WKT
sc=CRS('PROJCS["Brazil / Albers Equal Area Conic (WGS84)",GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.01745329251994328,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Albers_Conic_Equal_Area"],PARAMETER["longitude_of_center",-50.0],PARAMETER["standard_parallel_1",10.0],PARAMETER["standard_parallel_2",-40.0],PARAMETER["latitude_of_center",-25.0],UNIT["Meter",1.0]]')

print(sc) # Inspecionando o objeto sc
print("--------------------------------------------------------------")

# CRIANDO CÓPIA DO GEODATAFRAME COM O CRS CRIADO
bra_BRAlbers = bra.to_crs(crs = sc)
print(bra_BRAlbers.crs)
print("--------------------------------------------------------------")

print(bra_BRAlbers['geometry'].head()) # Checando a coluna geometria
print("--------------------------------------------------------------")

# CRIANDO CÓPIA DO GEODATAFRAME MODIFICANDO O CRS

# Rojetando os dados para Gall-Peters usando o proj4 string (texto no formato proj4) 

# Criando CRS baseado em proj4 string
sc=CRS('+proj=cea +lon_0=0 +lat_ts=45 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs')
bra_gall=bra.to_crs(crs=sc)
print(bra_gall.crs)
print("--------------------------------------------------------------")

# Reprojetar os dados para Estereografica do Polo Sul usando o string proj4. 
sc=CRS('+proj=stere +lat_0=-90 +lat_ts=-90 +lon_0=-63 +k=1 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs')
bra_ester=bra.to_crs(crs=sc)
print(bra_ester.crs)
print("--------------------------------------------------------------")

print(bra_ester['geometry'].head()) # Checando a coluna geometria 