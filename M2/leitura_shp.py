# LEITURA DE ARQUIVOS SHAPEFILE #
import geopandas as gpd # 'gpd' é o "apelido" pelo qual a biblioteca será chamada do script

# Caminho do shapefile
shapefile = "M2/arquivos_aulas/dis_sampa_23s.shp"

dis_sampa = gpd.read_file(shapefile) # Leitura

# Verifica o tipo de variável do shapefile
print(type(dis_sampa))

# Primeiros registros do geodataframe
print(dis_sampa.head(10))