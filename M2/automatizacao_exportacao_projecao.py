import geopandas as gpd

shapefile = "M2/arquivos_aulas/dis_sampa_23s.shp"
dis_sampa = gpd.read_file(shapefile)

# A variável sp_nome armazena o nome do distrito da geometria, por isso é necessário agrupar o GeoDataframe com base nesse atributo
agrupado=dis_sampa.groupby("sp_nome")
print(agrupado)
print("--------------------------------------------------------------")

# Iteramos sobre os dados agrupados
for key, values in agrupado:
    cod_dis = values
    
print(cod_dis) # Checando o último grupo sobre o qual foi iterado
print("--------------------------------------------------------------")

# Checando o tipo de dados do objeto agrupado e qual o valor da variável key
print(type(cod_dis))
print(key)
print("--------------------------------------------------------------")