# CONSULTAS ESPACIAIS: INTERSECT() E TOUCHES() #
from shapely.geometry import LineString, MultiLineString
import matplotlib.pyplot as plt
import geopandas as gpd

# Geometrias de linhas
la=LineString([(0,0),(1,1)])
lb=LineString([(1,1),(0,2)])

ml = MultiLineString([la, lb]) # Criando um objeto multilinha

# UTILIZAÇÃO DO "INTERSECTS"
intersecao = la.intersects(lb) # Verificando se as linhas se intersectam
intersecao_lb = lb.intersects(ml) # Checando se a linha se intersecta

# UTILIZAÇÃO DO "TOUCHES"
toque = la.touches(lb) # Verificando se as linhas se tocam
toque_lb = lb.touches(ml) # Checando se a linha b se toca

# Mostrando os resultados das consultas espaciais
print(f"As linhas se intersectam? {intersecao}")
print("--------------------------------------------------------------")

print(f"As linhas se tocam? {toque}")
print("--------------------------------------------------------------")

print(f"lb e ml se intersectam? {intersecao_lb}")
print("--------------------------------------------------------------")

print(f"lb e ml se tocam? {toque_lb}")

# Plotando as linhas
fig, ax = plt.subplots()
ax.plot(*la.xy, label='Linha A', marker='o')
ax.plot(*lb.xy, label='Linha B', marker='o')
ax.set_aspect('equal', adjustable='box')  # Para garantir que a escala seja a mesma nos dois eixos
ax.legend()

plt.savefig('M3/resultados/intersect_touches/multilinhas.png') # Salvando como imagem

gdf = gpd.GeoDataFrame(geometry=[ml])
gdf.to_file('M3/resultados/intersect_touches/multilinhas.shp') # Salvando como shapefile

plt.show()