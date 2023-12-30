# EXERCÍCIOS M3 - TRABALHANDO COM GEOCODIFICAÇÃO E CONCATENAÇÃO ESPACIAL #

## E1 - Geocodifique áreas verdes
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from geopandas.tools import geocode

# a) Crie um .txt que nem o que utilizamos na aula (endereco.txt) para as localizações abaixo e salve como areas_verdes.txt. Adicione uma coluna chamada Local com apelidos ou nome curtos para cada área.
    # - Praça Afonso Pena, São José dos Campos
    # - Praça Ouro Preto, São José dos Campos
    # - Praça Caratinga, São José dos Campos
    # - Centro Poliesportivo Vila Tesouro, São José dos Campos
    # - Praça Mario Porto, São José dos Campos
    # - Centro da Juventude, São José dos Campos
    # - Parque Vicentina Aranha, São José dos Campos
areas_verdes = "M3/aquivos_aula/areas_verdes.txt"
areas = pd.read_csv(areas_verdes, sep =';')

areas['Local'] = [
    "Afonso Pena",
    "Ouro Preto",
    "Caratinga",
    "Vila Tesouro",
    "Mario Porto",
    "Centro Juventude",
    "Vicentina Aranha"
]


# b) Geocodifique os endereços
geo = geocode(areas['Endereço'], provider = "nominatim", user_agent = "PyGEO_tutorial", timeout = 5)

# c) Reprojete as geometrias para WGS84 UTM Zona 23S
geometr = geo.to_crs(crs = "EPSG:32723")

# d) Faça uma concatenação baseada em atributo para obter a coluna local da tabela original
areas_geocodificadas = gpd.GeoDataFrame(pd.concat([areas, geometr], axis=1), geometry= geometr.geometry)

# e) Exporte como um shapefile com o nome areas_verdes.shp
areas_geocodificadas.to_file("M3/exercicios/resultados/areas_verdes.shp")

## E2 - Crie buffers ao redor das áreas verdes
# a) Crie uma nova coluna no GeoDataFrame para armazenar o buffer
areas_geocodificadas['Buffer'] = None

# b) Use a função buffer da Geopandas
areas_geocodificadas['Buffer'] = areas_geocodificadas['geometry'].buffer(distance= 0.100)

# c) Crie uma cópia do GeoDataFrame original e subtitua as geometrias nele pelos polígonos do buffer
area_buffer = areas_geocodificadas.copy()
area_buffer['geometry'] = area_buffer['Buffer']

## E3 - Quantas pessoas vivem em um raido de 1km dessa áreas verdes
# a) Importe o arquivo pop_sjc.shp
populacao = gpd.read_file('M3/resultados/cocatenacao/pop_sjc.shp')

# b) Execute a concatenação espacial entre o buffer e os setores censitários
areas_agrupadas = gpd.sjoin(area_buffer.to_crs(epsg=4674), populacao.to_crs(epsg=4674), op='intersects', how='left')

# c) Agrupe o geodataframe pelo nome de cada área verde
areas_agrupadas = areas_agrupadas.groupby('Local').agg({'pop': 'sum', 'geometry': 'first', 'Cod_setor': 'first'}).reset_index()

print(areas_agrupadas)

# d) Calcule a soma da população vivendo à 1km para cada área verde.
areas_agrupadas['populacao_1km'] = areas_agrupadas['pop'] - areas_agrupadas['pop'].shift(1).fillna(0)

# e) Insira a população total no GeoDataFrame do buffer
area_buffer = area_buffer.merge(areas_agrupadas[['Local', 'pop']], on= 'Local', how='left')

print(area_buffer)