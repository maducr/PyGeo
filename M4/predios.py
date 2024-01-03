# SALVANDO COMO SHAPEFILE #
import osmnx as ox
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

lugar = "Vila Ema, São José dos Campos"

predios = ox.geometries_from_place(lugar, tags = {"building":True})

predios_sub = predios[["geometry", "building"]]
print(predios_sub.head())

predios_sub.to_file('M4/resultados/predios.shp')