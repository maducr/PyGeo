from shapely.geometry import Point, LineString, Polygon

mundo_ext = [(-180, 90), (-180, -90), (180, -90), (180, 90)]
buraco = [[(-170, 80), (-170, -80), (170, -80), (170, 80)]]

mundo = Polygon(shell= mundo_ext) # shell -> casca

mundo_buraco = Polygon(
    shell = mundo_ext, # shell -> casca
    holes = buraco # holes -> buracos
)

print(mundo)
print('~~~~~~~~')
print(mundo_buraco)
print('~~~~~~~~')
print(type(mundo_buraco))

print('--------------------------------------------')

# Extrair popriedades #

cent_mundo = mundo.centroid # centroide
area_mundo = mundo.area # area
bbox_mundo = mundo.bounds # retangulo envolvente
mundo_fora = mundo.exterior # limite exterior
mundo_ext_comp = mundo.length

print('Centroide do polígono:', cent_mundo)
print('~~~~~~~~')
print('Área do polígono:', area_mundo)
print('~~~~~~~~')
print('Retângulo envolvente:', bbox_mundo)
print('~~~~~~~~')
print('Exterior do polígono:', mundo_fora)
print('~~~~~~~~')
print('Comprimento do exterior do polígono:', mundo_ext_comp)