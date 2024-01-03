from shapely.geometry import Point, LineString, Polygon
# Point - ponto
# LineString - linha
# Polygon - polígonos

# -------- PONTOS -------- #

p1= Point(5.4, 3.0)
p2= Point(10, -7)
p3= Point(80, 25)

# -------- LINHA -------- #

linha = LineString([p1, p2, p3])
linha2 = LineString ([(5.4, 3.0), (10, -7), (80, 25)])

print(linha)
print(type(linha))
print('~~~~~~~~')
print(linha2)
print(type(linha2))

print('--------------------------------------------')

# Valor exato da coordenada #
lxy = linha.xy
print(lxy)

print('--------------------------------------------')

# Extrair separadamente
lx = lxy[0] # acessar o primeiro objeto da variável lxy 
ly = lxy[1] # acessar o segundo objeto da variável lxy

print(lx)
print('~~~~~~~~')
print(ly)

print('--------------------------------------------')

# Comprimento de linha # -> km
# comp 

l_comp = linha.length # length - comprimento
l_cent = linha.centroid # centroid - centroide

tipo_cent = type(l_cent)

print('O comprimento da linha é: %s' %(round(l_comp, 2)))
print('O centroide da linha é: %s' %(l_cent))
print('Tipo de dados do centroide: %s' %(tipo_cent))