# EXERCÍCIOS M1 - TRABALHANDO COM GEOMETRIAS #
# E1 - Criando geometrias básicas e obtendo seus atributos
from geopy.distance import geodesic
from shapely.geometry import Point, LineString, Polygon, MultiPoint
from d1 import criar_ponto, criar_linha, calcular_area_e_centroide, gerar_retangulo_envolvente, criar_multiponto

# a) Use o Google Maps para obter as coordenadas (Longitude, Latitude) dos cinco lugares que você mais gosta na sua cidade. Crie um objeto do tipo Point (ponto) para cada um desses lugares. Descubra qual desses locais fica a uma maior distância um do outro e quanto é essa distância. Mostre na tela o tipo de objeto de cada um dos pontos.

ped = criar_ponto(-8.88, -63.83)  # pedreira
inov = criar_ponto(-8.75, -63.90)  # inove
cens = criar_ponto(-8.70, -63.89)  # censipam
cine = criar_ponto(-8.74, -63.87)  # cine araujo
parque = criar_ponto(-8.76, -63.90)  # parque da cidade

# Lista
pontos = [ped, inov, cens, cine, parque]

maior_distancia = 0
ponto1 = None
ponto2 = None

# Distância entre cada par de pontos
for i in range(len(pontos)):
    for j in range(i + 1, len(pontos)):
        distancia = geodesic(
            (pontos[i].y, pontos[i].x),
            (pontos[j].y, pontos[j].x)
        ).kilometers
        if distancia > maior_distancia:
            maior_distancia = distancia
            ponto1 = pontos[i]
            ponto2 = pontos[j]

print('A maior distância é %s km.' % round(maior_distancia, 2))
print(f'Os pontos correspondentes são {ponto1} e {ponto2}.')
print('--------------------------------------------')

# b) Crie um objeto do tipo linha (LineString) que conecta esses cinco locais. Mostre na tela o tipo de objeto dessa linha e obtenha seu comprimento total.

linha_ref = criar_linha([ped, inov, cens, cine, parque])

l_comp = linha_ref.length

print(linha_ref)
print(type(linha_ref))
print('O comprimento total da linha é: %s' % round(l_comp, 2))
print('--------------------------------------------')

# c) Descubra a área e o centróide do polígono que tem esses cinco locais como vértices.
vertices_desafio = [[p.x, p.y] for p in [ped, inov, cens, cine, parque]]
area, centroide = calcular_area_e_centroide(vertices_desafio)
retangulo_envolvente = gerar_retangulo_envolvente(vertices_desafio)
multiponto_desafio = criar_multiponto([ped, inov, cens, cine, parque])

print(f'A área do polígono é {round(area, 2)} e seu centróide é {centroide}')
print(f'O retângulo envolvente do polígono é: {retangulo_envolvente}')
print(f'Multiponto: {multiponto_desafio}')
print('--------------------------------------------')

# d) Gere o retângulo envolvente do polígono gerado em c.
retang_plg = gerar_retangulo_envolvente(vertices_desafio)

print(f'O retângulo envolve do polígono é: {retang_plg}.')
print('--------------------------------------------')

# e) Crie uma coleção de geometrias do tipo Multiponto (MultiPoint) para armazenar a localização desses cinco lugares
multi_pts = criar_multiponto([ped, inov, cens, cine, parque])
print(f'Multiponto: {multi_pts}')
print('--------------------------------------------')

# E2 - Criando geometrias a partir de coordenadas de um arquivo de texto
# DICA: Use a função pandas.read_csv para ler os arquivos .txt, verifique o separador utilizado antes de importar o arquivo.
from geopy.distance import geodesic
from shapely.geometry import Point, LineString
import pandas as pd

# Leitura do arquivo de texto
arquivo = 'M1/exercícios-desafios/coordenadas.txt'
dados_onibus = pd.read_csv(arquivo)

# a) Crie geometrias do tipo Point para representar as paradas de ônibus
paradas_geometrias = [Point(xy) for xy in zip(dados_onibus['Longitude'], dados_onibus['Latitude'])]

# b) Crie um objeto do tipo LineString para representar a linha de ônibus número 177
paradas_177 = dados_onibus[dados_onibus['Linha'] == 177]
linha_177 = criar_linha([Point(xy) for xy in zip(paradas_177['Longitude'], paradas_177['Latitude'])])

# c) Crie objetos do tipo LineString para representar cada uma das linhas de ônibus
linhas_onibus = {}
for linha, paradas in dados_onibus.groupby('Linha'):
    linhas_onibus[linha] = criar_linha([Point(xy) for xy in zip(paradas['Longitude'], paradas['Latitude'])])

# d) Calcule o comprimento médio das linhas de ônibus
comprimentos = [linha.length for linha in linhas_onibus.values()]
comprimento_medio = sum(comprimentos) / len(comprimentos)

# Resultados
print(f'Objeto LineString da linha 177: {linha_177}')
print(f'Objetos LineString para cada linha de ônibus: {linhas_onibus}')
print(f'Comprimento médio das linhas de ônibus: {round(comprimento_medio, 2)} km')