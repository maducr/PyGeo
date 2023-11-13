from shapely.geometry import Point, LineString, Polygon
# Point - ponto
# LineString - linha
# Polygon - polígonos

# -------- PONTOS -------- #

p1= Point(5.4, 3.0)
p2= Point(10, -7)
p3= Point(80, 25)
p3D= Point(5.4, 3.0, 25)

print(p1)
print(p3D)

print(type(p2)) # type - tipo
print(type(p3))

print('--------------------------------------------')

# Estrair a sequência de coordenadas do ponto # 
# coords

p_coords = p1.coords
print(p_coords)
print(type(p_coords))

print('--------------------------------------------')

# Valor exato da coordenada - pontos #
xy = p_coords.xy
print(xy)

print('--------------------------------------------')

# Extraindo separadamente 
x = p1.x
y = p1.y
print(x)
print('~~~~~~~~')
print(y)

print('--------------------------------------------')

# Distâncias entre pontos e coordenadas de entrada #
p_dist = p1.distance(p2)
print('A distância entre os pontos é de %s graus decimais' %(round(p_dist, 2)))