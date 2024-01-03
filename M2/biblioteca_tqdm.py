# AUTOMATIZAÇÃO DE EXPORTAÇÃO E PROJEÇÃO DE SHAPEFILES #
import os
import geopandas as gpd
from tqdm import tqdm
import re

# Carregando o shapefile inicial
shapefile = "M2/arquivos_aulas/dis_sampa_23s.shp"
dis_sampa = gpd.read_file(shapefile)

# Agrupando por "sp_nome"
agrupado = dis_sampa.groupby("sp_nome")

# Pasta de saída
saida = r"M2/salvando-shp-resultados/m2.6"
pasta_resultado = os.path.join(saida, "Distritos")

# Criando a pasta de resultados se não existir
if not os.path.exists(pasta_resultado):
    os.makedirs(pasta_resultado)

# Pasta de resultados reprojetados
pasta_reproj = os.path.join(pasta_resultado, "Reproj")

# Criando a pasta de resultados reprojetados se não existir
if not os.path.exists(pasta_reproj):
    os.makedirs(pasta_reproj)

# Iterando sobre os dados agrupados
for key, values in tqdm(agrupado, desc="Exportando Shapefiles"):
    # Sanitizando o nome para remover caracteres especiais
    nome_saida = "%s.shp" % re.sub(r'[^\w\s]', '', key.replace(" ", "_"))

    # Caminho de saída para salvar o arquivo
    outpath = os.path.join(pasta_resultado, nome_saida)

    # Exportando dados para shapefile
    values.to_file(outpath)

print("----------------------------------------------------------------")

# REPROJEÇÃO
shapefiles = [file for file in os.listdir(pasta_resultado) if file.endswith(".shp")]

print(shapefiles)  # Verificando resultados
print("----------------------------------------------------------------")

# Usando loop for para iterar e projetar cada shapefile
for shapefile in shapefiles:
    # Lendo o arquivo shapefile
    dados = gpd.read_file(os.path.join(pasta_resultado, shapefile))

    # Reprojetando para EPSG 4326
    dados = dados.to_crs("epsg:4326")

    # Exportando o GeoDataFrame reprojetado como shapefile
    nome_reproj = "repro_%s" % shapefile
    outpath_reproj = os.path.join(pasta_reproj, nome_reproj)
    dados.to_file(outpath_reproj)

print("Concluído!")
