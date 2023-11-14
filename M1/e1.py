from geopy.distance import geodesic
from shapely.geometry import Point
# EXERCÍCIOS M1 - TRABAÇLHANDO COM GEOMETRIAS #
# E1 - Criando geometrias básicas e obtendo seus atributos

# a) Use o Google Maps para obter as coordenadas (Longitude, Latitude) dos cinco lugares que você mais gosta na sua cidade. Crie um objeto do tipo Point (ponto) para cada um desses lugares. Descubra qual desses locais fica a uma maior distância um do outro e quanto é essa distância. Mostre na tela o tipo de objeto de cada um dos pontos.

ped = Point(-8.88, -63.83) # pedreira
inov = Point(-8.75, -63.90) # inove
cens = Point(-8.70, -63.89) # censipam
cine = Point(-8.74, -63.87) # cine araujo
parque = Point(-8.76, -63.90) # parque da cidade

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

print('A maior distância é %s km.' %round(maior_distancia, 2))
print(f'Os pontos correspondentes são {ponto1} e {ponto2}.')