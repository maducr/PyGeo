# DESAFIO E1 - CRIE E TESTE FUNÇÕES QUE EXECUTEM AS SEGUINTES TAREFAS (EXERCÍCIOS EX1)
# Os exercícios desafio são uma excelente oportunidade para expandir suas habilidades como programador(a).

# DICAS: Escreva uma função que cria geometrias de pontos e outra que cria geometrias de linha.
from shapely.geometry import Point, LineString, Polygon, MultiPoint

def criar_ponto(lat, lon):
    return Point(lon, lat)

def criar_linha(coordenadas):
    return LineString(coordenadas)

def calcular_area_e_centroide(vertices):
    poligono = Polygon(vertices)
    return poligono.area, poligono.centroid

def gerar_retangulo_envolvente(vertices):
    poligono = Polygon(vertices)
    return poligono.envelope

def criar_multiponto(pontos):
    return MultiPoint(pontos)