# CONSULTAS ESPACIAIS: CONTAINS() E WITHIN() #

# A função .within() que checa se o pontos está dentro do polígono
# A função .contains() que checa se um polígono contém um ponto
from shapely.geometry import Point, Polygon

# Geometrias de ponto
p1=Point(51.1103009,17.038199)
p2=Point(51.106977,17.016376)

plg=Polygon([(51.114671, 17.022160),(51.108502, 17.022468),(51.104253, 17.041725),(51.112447, 17.044875)])

# Mostrando o conteúdo de cada objeto
print(p1)
print(p2)
print(plg)
print("--------------------------------------------------------------")

# UTILIZAÇÃO DO "WITHIN"
print(p1.within(plg)) # Checando se o ponto p1 está dentro do polígono
print("--------------------------------------------------------------")

print(p2.within(plg)) # Checando se o ponto p2 está dentro do polígono
print("--------------------------------------------------------------")

# UTILIZAÇÃO DO "CONTAIN"
print(plg.contains(p1)) # Checando se o polígono plg contem o p1
print("--------------------------------------------------------------")

print(plg.contains(p2)) # Checando se o polígono plg contem o p2

# QUANDO UTILIZAR:
# - Relação espacial entre muitos pontos e apenas um polígono: Se você quiser descobrir quais pontos estão dentro do polígono, você precisa iterar sobre os pontos e verificar um de cada vez com a função contains().
# - Relação espacial entre um ponto e vários polígonos: Se você quiser descobrir quais polígonos contém o ponto, você precisa iterar sobre os polígonos com a função within() até encontrar o polígono que retorne True para o ponto especificado.