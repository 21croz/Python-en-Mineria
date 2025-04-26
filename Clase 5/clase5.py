import pandas as pd
import matplotlib.pyplot as plt


# # Importar la base de datos.
# df = pd.read_table('Bases de datos/database.txt', sep = ' ')
# print(df)

# Definir los ejes del gráfico
# ejex = df['X']
# ejey = df['Y']

# etiquetas = ['Linea']

# # Crear el gráfico.
# plt.scatter(ejex, ejey, label = etiquetas)

# plt.xlabel('Eje x')
# plt.ylabel('Eje y')
# plt.title('Mi primer gráfico en Matplotlib')
# plt.legend()

# # Mostrar el gráfico.
# plt.show()

# df2 = pd.read_table('Bases de datos/modelo2.txt', sep = '\t')

# datos = df2['CUT']

# plt.hist(datos, bins = 8, color = 'pink', edgecolor = 'black')

# plt.xlabel('Ley de cobre [%]')
# plt.ylabel('Frecuencia')
# plt.title('Histograma de la dispersión de ley de cobre.')

# plt.show()


# 1 fila y 2 columnas.
fig, ax = plt.subplots(1, 2)

ax[0].plot([8, 15, 12, 21], [3, 4, 7, 1])
ax[0].set_title('Gráfico 1')

ax[1].bar([10, 14, 4, 9, 2], [22, 13, 6, 0, 5])
ax[1].set_title('Grafico 2')

plt.tight_layout()
plt.show()