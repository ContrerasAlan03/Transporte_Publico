import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#variable donde se almacena el dataframe
#Descarga el archivo de Excel y pega la ruta en este espacio donde guardo ese archivo
archivo = 'C:/Users/Alan/Documents/Transmetro_2.xlsx'

df = pd.read_excel(archivo, sheet_name = 'Transmetro')

#creacion
estacion = nx.from_pandas_edgelist(df, source='Origen', target='Destino', edge_attr='Longitud')
estacion.nodes()
estacion.edges()
estacion.order()

#vertices
print("Listado de estaciones: ")
print(estacion.nodes())

#Aristas
print("\nRecorridos: ")
print(estacion.edges())

#cantidad
#cantidad de vertices
print("\nCantidad de estaciones: ")
print(estacion.order())

# Calculo de ruta con dijkstra
ruta1= nx.dijkstra_path(estacion, source='Pacho Galan', target='Buenos Aires', weight='Longitud')

#Ruta mas corta
print("\nRuta: ")
print(ruta1)

#Cantidad de estaciones por la que pasa
print("\n Cantidad de estaciones por la que pasa: ")
print(len(ruta1))

#Cantidad de metros recorridos
print("\nDistancia en metros Recorridos: ")
print((nx.dijkstra_path_length(estacion, 'Pacho Galan', 'Buenos Aires', 'Longitud')))


# Graficas

# Obtener el número de estaciones por ruta
estaciones_por_ruta = [len(nx.dijkstra_path(estacion, source='Pacho Galan', target='Buenos Aires', weight='Longitud'))
    for destino in estacion.nodes()]

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(range(len(estaciones_por_ruta)), estaciones_por_ruta)
plt.xlabel('Ruta')
plt.ylabel('Cantidad de estaciones')
plt.title('Cantidad de estaciones por ruta')
plt.xticks(range(len(estaciones_por_ruta)), estacion.nodes(), rotation=90)
plt.tight_layout()
plt.show()
