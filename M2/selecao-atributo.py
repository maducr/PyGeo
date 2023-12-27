# SELEÇÃO POR ATRIBUTOS #
import geopandas as gpd

# Caminho do shapefile
shapefile = "M2/arquivos_aulas/dis_sampa_23s.shp"

dis_sampa = gpd.read_file(shapefile)

print(dis_sampa.head(3))

print("---------------------------------------------------------------------------------------------------------------")

# Selecionando apenas a geometria que tem o atributo "ds_nome" igual à MOEMA
moema = dis_sampa[dis_sampa.ds_nome == "MOEMA"] # A igualdade comparativo é expressa por duplo sinal de igualdade (==)

# Resultado
print(moema)

# SALVANDO O SHP CRIADO
out = "M2/salvando-shp-resultados/moema.shp" # Caminho para salvar como shapefile os dados selecionados

moema.to_file(out) # Exportando o geodataframe como shapefile 