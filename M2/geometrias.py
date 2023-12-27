# INTRODUÇÃO À GEOMETRIAS NA GEOPANDAS #
import geopandas as gpd

shapefile = "M2/arquivos_aulas/dis_sampa_23s.shp"

dis_sampa = gpd.read_file(shapefile)

print(dis_sampa["geometry"].head())

print("----------------------------------------------------------------")

# CALCULANDO ÁREA
for index,row in dis_sampa[0:5].iterrows():
    #print(row)
    #print("---------------------------------")
    #print(index)
    #print("---------------------------------")
    plg_area = row["geometry"].area
    print("A área de {0} é: {1:.2f}".format(row["ds_nome"], plg_area)) # Mostra na tela a área calculada e o nome de cada distrito
    
print("------------------------------------------------------------------------------------------------------------------------")

# ÁREA EM KM^2
dis_sampa['area_km2'] = dis_sampa.area/1000000

print(dis_sampa.head())

print("------------------------------------------------------------------------------------------------------------------------")

# VALOR MÉDIO E MÁXIMO
max_area = dis_sampa["area_km2"].max()
ave_area = dis_sampa["area_km2"].mean()

print("Área máxima: %s \nÁrea média: %s" %(round(max_area, 2), round(ave_area,2)))