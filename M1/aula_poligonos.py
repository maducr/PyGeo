from shapely.geometry import Point, LineString, Polygon
# Point - ponto
# LineString - linha
# Polygon - polígonos

# -------- PONTOS -------- #

p1= Point(5.4, 3.0)
p2= Point(10, -7)
p3= Point(80, 25)

# -------- POLÍGONOS -------- #

# Passando coordenadas # 
plg = Polygon([(5.5, 4.2), (10, -1), (8, 5)])

# Importando pontos #
plg2 = Polygon([[p.x, p.y] for p in [p1, p2, p3]]) # Compreenção de lista - forma reduzida de fazer um loop

plg_tipo = plg.geom_type 
plg_tipo2 = type(plg)

print(plg)
print('~~~~~~~~')
print(plg2)

print('--------------------------------------------')

print('Tipo da geometria em formato de texto: %s' %(plg_tipo))
print('Tipo da geometria como o Python geralment mostra: %s' %(plg_tipo2))
