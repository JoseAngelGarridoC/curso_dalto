import pandas as pd

# Usando la función read_csv para leer el archivo .csv
df = pd.read_csv('archivo//datos.csv') # df => dataframe: estructura de datos bidimensionales (fila - columna)
df2 = pd.read_csv('archivo//datos.csv')
# Obteniendo los datos de la columna nombre
nombre = df['nombre']
#print(nombre)

# Ordenando el dataframe por la edad de forma ascendente
ordenando_valores = df.sort_values('edad')

# Ordenandolo de forma descendente
ordenando_valores = df.sort_values('edad', ascending=False)
#print(ordenando_valores)

# Concatenando 
concatenando = pd.concat([df,df2])
#print(concatenando)

# Accediendo a la primeras filas
primera_fila = df.head(2)
#print(primera_fila)

# Accediendo a las últimas filas
ultimas_filas = df.tail(2)
#print(ultimas_filas)

# Accediendo a la cantidad de filas columnas
filas_columnas = df.shape # shape me muestra la cantidad de filas y columnas en el .csv
#print(filas_columnas)

num_filas, num_columnas = df.shape
#print(f'Números de filas: {num_filas}')
#print(f'Números de columnas: {num_columnas}')

# Obteniendo data estdística del df
df_info = df.describe()
#print(df_info)

# Accediendo a elemento específico
elemt_espesif = df.loc[1,'nombre']
#print(elemt_espesif)

# Accediendo a elemento específico
elemt_especif = df.loc[:,'apellido']
#print(elemt_especif)

# Accediendo a elemento específico 
elemt_especif = df.loc[3,:] 
#print(elemt_especif)

'''
    NOTA: Con .iloc[:] ocurre exactamente lo mismo. Observa la fila 65
'''

# Accediendo a elemento espesífico con iloc
elemt_con_iloc = df.iloc[2,2]
#print(elemt_con_iloc)

# Accediendo a elemento espesífico con iloc
elemt_con_iloc = df.iloc[:,0]
#print(elemt_con_iloc)

# Accediendo a elemento espesífico con iloc
elemt_con_iloc = df.iloc[3,:]
#print(elemt_con_iloc)

# Accediendo a filas menores de 30 años
mayores_a_treinta = df.loc[df['edad']<30,:]
print(mayores_a_treinta)