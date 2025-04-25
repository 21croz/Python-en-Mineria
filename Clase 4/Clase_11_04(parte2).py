import pandas as pd

df = pd.read_table('modelo2.txt', sep = '\t', header = 0)

volumen_bloque = 10*10*10 # m^3
df['TON'] = volumen_bloque*df['DENSITY']

df['Cu_Q'] = (df['CUT']/100)*df['TON']

col_CUT = df['CUT'].tolist()