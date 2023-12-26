from shapely import geometry
from shapely.geometry import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, box

# -------- PONTOS -------- #

p1= Point(5.4, 3.0)
p2= Point(10, -7)
p3= Point(80, 25)

# -------- MULTIPLOS PONTOS -------- #

multi_pts = MultiPoint([p1, p2, p3]) 
multi_pts2 = MultiPoint([(2.2, 10), (4, -10), (25.4, -3)]) # Coordenadas separadas

# -------- MULTIPLAS LINHAS -------- #

l1 = LineString([p1, p2])
l2 = LineString([p2, p3])

multi_linha = MultiLineString([l1, l2])

# -------- MULTIPLOS POLÍGONOS -------- #
# Os polígonos iram repreentar os emisférios do mundo

oc_ext = [(-180, 90), (-180, -90), (0, -90), (0, 90)]
oc_bur = [[(-170, 80), (-170, -80), (-10, -80), (-10, 80)]]

oc_pol = Polygon (
    shell = oc_ext,
    holes = oc_bur
)

# Representando polígonos - box
min_x, min_y = 0, -90
max_x, max_y = 180, 90

or_box = box(minx=min_x, miny=min_y, maxx=max_x, maxy=max_y)

multi_plg = MultiPolygon([oc_pol, or_box])

# Polígono convexo
conv_pol = multi_pts.convex_hull

# Número de linhas em um objeto multilinha #
n_lin = len(multi_linha.geoms)

# Cálculo área
mlt_plg_area = multi_plg.area # a área do furo é excluida

# Multigeometrias - indeses 
oc_area = multi_plg.geoms[0].area

# Validando geometrias
val = multi_plg.is_valid

print('Polígono convexo dos pontos:', conv_pol)
print('~~~~~~~~')
print('Número de linhas:', n_lin)
print('~~~~~~~~')
print('Área dos multipolígonogos:', mlt_plg_area)
print('~~~~~~~~')
print('Área do hemisfério ocudental:', oc_area)
print('~~~~~~~~')
print('A geometria é válida?', val)