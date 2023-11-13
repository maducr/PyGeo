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

