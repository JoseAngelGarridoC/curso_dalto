'''
Las funciones lambda crea funciones anónimas que después podemos guardar
en variables
'''

potencia_de_dos = lambda x: x**2

print(potencia_de_dos(5))

# Ejemplo de dos funciones sin lambda:
    # Primera función
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Creando función común que diga si es par o no
def num_par(x):
    if (x % 2 == 0): # Si colocamos 1 no dará los números impares
        return True

# Usando filter con una función común
los_pares = filter(num_par,numeros)   
print(list(los_pares))

    # Segunda función:
sex = ['hombre','mujer','mujer','hombre','hombre','mujer','mujer','hombre','hombre','mujer','mujer','hombre']

# Creando función común que me dé solo las mujeres
def sexo(x):
    if (x == 'mujer'): # Si colocamos hombre nos dará solo los string hombre
        return True

# Usando filter con una función común
los_sexos = filter(sexo,sex)   
print(list(los_sexos))

# Ahora las mismas funciones pero con lambda:
print()
print('Ahora las mismas funciones pero con lambda:')

#los_pares = lambda x: x % 2 == 0
#los_pares = filter(num_par,numeros)
los_pares = filter(lambda x: x % 2 == 0,numeros)  
print(list(los_pares))
print()

#los_sexos = lambda x: x == 'mujer'
#los_sexos = filter(sexo,sex)
los_sexos = filter(lambda x: x == 'mujer',sex)   
print(list(los_sexos))