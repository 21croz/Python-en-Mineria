import pandas as pd

data = {
    'Nombre': ['Ana', 'Luis', 'Pedro', 'Carla', 'Jorge', 'Lucía', 'Andrés', 'Sofía', 'Marcos', 'Valeria'],
    'Edad': [15, 30, 17, 22, 35, 8, 24, 26, 31, 2],
    'Pais': ['España', 'México', 'Chile', 'Colombia', 'Argentina', 'Perú', 'Uruguay', 'Ecuador', 'Bolivia', 'Paraguay']
}

df = pd.DataFrame(data)

# Crear columna con la cantidad de meses
df['Meses'] = df['Edad']*12

# Crear la columna Adulto, que contiene 1 si la persona es mayor
# y 0 si la persona es menor de edad.
df['Adulto'] = 0
df['Adulto'][df['Edad'] >= 18] = 1

# Usar funcion iterrows
# for index, row in df.iterrows():
#     print(f'Persona {index + 1}')
#     print(f'Soy {row['Nombre']}, tengo {row['Edad']} años y soy de {row['Pais']}')
#     print(' ')

