import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_table('modelo2.txt', sep = '\t', header = 0)


cutoff_grades = np.arange(0, 5.5, 0.1)
vol = 10*10*10
df['TON'] = vol*df['DENSITY']
df['fino'] = (df['CUT']/100)*df['TON']


cummulated_tonnage = []
mean_grade = []


for gc in cutoff_grades:
    tonnage = df['TON'][df['CUT'] >= gc].sum()
    fines = df['fino'][df['CUT'] > gc].sum()

    cummulated_tonnage.append(tonnage)
    mean_grade.append(fines / tonnage*100)




fig, ax_tonn = plt.subplots()
plt.title('Curva tonelaje-ley')

ax_tonn.set_xlabel('Ley de corte de Cu [%]')
ax_tonn.set_ylabel('Tonelaje acumulado [ton]')
line_1, = ax_tonn.plot(cutoff_grades, cummulated_tonnage, 'r', label='tonnage')

ax_grade = ax_tonn.twinx()
ax_grade.set_ylabel('Ley media de Cu [%]')
line_2, = ax_grade.plot(cutoff_grades, mean_grade, 'g', label='grade')

lines = [line_1, line_2]
labels = [line.get_label() for line in lines]
ax_tonn.legend(lines, labels, loc='upper right')

plt.show()