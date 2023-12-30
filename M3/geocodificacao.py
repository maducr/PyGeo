# GEOCODIFICAÇÃO #
import pandas as pd

uploaded = "M3/aquivos_aula/enderecos.txt"

dados = pd.read_csv(uploaded, sep =';') # Leitura do arquivo endereco.txt como um dataframe para a variável dados

# print(dados.head())

# GEOCODE
from geopandas.tools import geocode

# help(geocode)

# CODIFICAÇÃO
geo = geocode(dados['Endereço'], provider = "nominatim", user_agent = "PyGEO_tutorial", timeout = 5) # Geocodificando os endereços da coluna "Endereço" do nosso dataframe utilizando o nominatim (provedor de geocodificação do OSM)

print(geo.head())
print("--------------------------------------------------------------")

# CONCATENAÇÃO DE TABELA

comb = geo.merge(dados, left_index = True, right_index = True) # Criando uma nova tabela usando a função merge para combinar os dados originais (dados) e a tabela com a geocodificação (combinando as tabelas com base em seus índices (index))

print(comb.head())
print("--------------------------------------------------------------")

print(type(comb)) # Verificação de tipo
print("--------------------------------------------------------------")

print(comb.crs) # Verificação de coordenadas dos dados
print("--------------------------------------------------------------")

# EXPORTANDO COMO SHAPEFILE
try:
    comb.to_file('M3/resultados/geocodificacao')
    print("Exportação bem-sucedida: M3/resultados.shp")
except Exception as e:
    print("Erro durante a exportação:", e)