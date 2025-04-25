import pandas as pd

# Crear base de datos
data = {
    'Nombre': ['Ana', 'Luis', 'Pedro', 'Carla', 'Jorge', 'Lucía', 'Andrés', 'Sofía', 'Marcos', 'Valeria'],
    'Edad': [15, 30, 17, 22, 35, 8, 24, 26, 31, 2],
    'Pais': ['España', 'México', 'Chile', 'Colombia', 'Argentina', 'Perú', 'Uruguay', 'Ecuador', 'Bolivia', 'Paraguay']
}

# Pasar a DataFrame
df = pd.DataFrame(data)

# Agregar cantidad de meses
df['Meses'] = df['Edad']*12

# Saber si es adulto
df['Adulto'] = 0
df['Adulto'][df['Edad'] >= 18] = 1


# Usar iterrows
for index, row in df.iterrows():
    print(f'Ella es {row['Nombre']}, tiene {row['Edad']} años y es de {row['Pais']}')




# df = pd.read_table('modelo2.txt', sep = '\t', header = 0)

# ley_corte = 2

# df['MINAR'] = 0
# df['MINAR'][df['CUT'] > ley_corte] = 1

# print(df)