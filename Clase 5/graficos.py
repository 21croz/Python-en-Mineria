import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Leemos el archivo con pandas.
df = pd.read_table('database.txt', sep = ' ')

# Definimos las variables con las columnas del archivo
x = df['X']
y = df['Y']

# Crear el gráfico.
# Para hacer un gráfico de puntos, cambiamos plot por scatter.
plt.plot(x, y)

# Etiquetas y títulos
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Grafico de la base de datos')

# Mostramos el gráfico.
plt.show()



# Para hacer un histograma solo es necesaria la columna con los valores (eje y).
plt.hist(y, bins = 5, color = 'skyblue', edgecolor = 'black')

plt.xlabel('X')
plt.ylabel('Frecuencia')
plt.title('Histograma')

plt.show()



fig, axs = plt.subplots(1, 2)  # 1 fila, 2 columnas.

axs[0].plot([1, 2, 3], [1, 4, 9])
axs[0].set_title("Gráfico 1")

axs[1].bar([1, 2, 3], [3, 2, 5])
axs[1].set_title("Gráfico 2")

plt.tight_layout()
plt.show()