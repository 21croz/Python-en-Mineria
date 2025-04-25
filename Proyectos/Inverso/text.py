import pandas as pd
from math import sqrt


def calcular_ley(x_pos, y_pos, datos):
    grade = 0
    for item in datos:
        distancia = sqrt((-)+(-))
    return


df = pd.read_table('database.txt', sep = ' ')

x_col = df['X'].tolist()
y_col = df['Y'].tolist()
grade_col = df['grade'].tolist()
tuples_list = list(zip(x_col, y_col, grade_col))

coords = set((row.X, row.Y) for row in df.itertuples(index = False))

for x in range(-100, 101):
    for y in range(-100, 101):
        if (x, y) not in coords:
            ex_count += 1

print(ex_count)