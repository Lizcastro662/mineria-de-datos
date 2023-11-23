import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mode

# Función para calcular la distancia euclidiana
def euclidean_distance(p_1, p_2):
    return np.sqrt(np.sum((p_2 - p_1) ** 2))

# Función para encontrar los k vecinos más cercanos
def k_nearest_neighbors(points, labels, input_data, k):
    input_distances = [
        [euclidean_distance(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    return [
        mode([labels[index] for index in point_nearest])
        for point_nearest in points_k_nearest
    ]

# Lectura del archivo CSV
file_path = r"C:\Users\lizca\Downloads\mineria de datos\base\datoslimpios.csv"
df = pd.read_csv(file_path)

# Imprimir las primeras filas del DataFrame para verificar la estructura
print(df.head())

# Realizar la clasificación con KNN (añadir aquí tu lógica de clasificación)

# Visualización de los datos clasificados en un gráfico de dispersión
plt.scatter(df['player_ranking'], df['tourney_year'])
plt.xlabel('Player Ranking')
plt.ylabel('Tournament Year')
plt.title('Classification')
plt.savefig(r"C:\Users\lizca\Downloads\mineria de datos\img\Classification.png")  # Guardar la imagen en la ubicación específica
plt.show()
