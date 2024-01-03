# EXERCÍCIOS M2 - TRABALHANDO COM SISTEMAS DE COORDENADAS #

# E1 - Crie um polígono a partir de uma lista de coordenadas
# DICAS: Para acessar o arquivo você precisa montar o Google drive (como fizemos nas aulas), ou carregar do seu computador para o Colab.
import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import re

# a) Crie um polígono a partir das coordenadas x e y dadas no arquivo coords.txt. O sistema de coordenadas desses dados é o EPSG 29183.
coordenadas = "M2/arquivos_aulas/coords.txt" # caminho do arquivos contendo as coordenadas

# Leitura do arquivo e extração das coordenadas
with open(coordenadas, 'r') as f:
    conteudo = f.read()

# Use a função re.split para quebrar o texto em múltiplos subtextos.
items = re.split(r'[\[\]]', conteudo)

# Use um loop para verificar em quantos e quais items o texto foi subdividido
for i in items:
    print(items.index(i))
    print(i)

coordenadas_list = [float(coord) for coord in items if coord.strip().replace('.', '').replace('-', '').isdigit()]

coords_list = list(zip(coordenadas_list[0::2], coordenadas_list[1::2]))

# b) Insira o polígono criado em um geodataframe
gdf = gpd.GeoDataFrame(geometry=[Polygon(coords_list)], crs="EPSG:29183")

# c) Salve o polígono em um shapefile
output_shapefile_path = "M2/exercícios/resultados"
gdf.to_file(output_shapefile_path)

# d) Plote e salve uma figura do polígono
gdf.plot()
plt.title('Polígono a partir de coords.txt')
plt.savefig("M2/exercícios/resultados/resoltado.png", dpi=300) # Salvando como imagem
plt.show()