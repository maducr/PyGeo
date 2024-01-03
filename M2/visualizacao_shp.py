# VISUALIZAÇÃO DE ARQUIVOS SHAPEFILE #
import geopandas as gpd  # 'gpd' é o "apelido" pelo qual a biblioteca será chamada do script
import matplotlib.pyplot as plt # 'plt' é o "apelido" pelo qual a biblioteca será chamada do script

# Caminho do shapefile
shapefile = "M2/arquivos_aulas/dis_sampa_23s.shp"

dis_sampa = gpd.read_file(shapefile)

# Cria a figura e os eixos para ploragem (tamanho 10x10 polegadas)
fig,ax = plt.subplots(figsize = (10,10))

# Plotagem
print(dis_sampa.plot(ax = ax))

# Nomeando os eixos y e x
ax.set_ylabel("EIXO NORTE-SUL")
ax.set_xlabel("EIXO OESTE-LESTE")

# Removendo a notação científica dos eixos 
ax.ticklabel_format(style = "plain")

# Rotacionando os rótulos numéricos do eixo y
plt.yticks(rotation = 90)

# Exibe o mapa
plt.show()