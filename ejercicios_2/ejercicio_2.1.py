'''
Faltó el profesor y los chicos van a armar la clase. Uno de
los alumnos será el profesor y otro será el asistente.
Programe lo siguiente:

    a) Pedir la edad de los compañeros que vinieron a la 
    clase y ordenar los datos de menor a mayor.

    b) Si el mayor de la clase es el profesor y el menor es 
    el asistente. ¿Quienes serán?
'''

# Función para obtener al asistente y al profesor según la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    # Creando la lista de compañeros
    compañeros = []
    
    # Ejecutando un for para pedir información de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input('Ingrese el nombre del compañero: ')
        edad = int(input('Ingrese la edad del compañero: '))
        compañero = (nombre, edad) # Esta es una tupla
        
        # Agregando información de la tupla a la lista
        compañeros.append(compañero)
        
    # Ordenándolos de menor a mayor según la edad
    compañeros.sort(key=lambda x: x[1])
    
    '''
        Compañeros[x] devuelve una tupla con (nombre, edad)
        y después accedemos al nombre para definir al profesor
        y al asistente
    '''
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    # Retornamos una tupla
    return asistente, profesor

# Desempaquetamos lo que nos retorna la función
asistente, profesor = obtener_compañeros(5) # => Aquí se llama a la función

# Mostrando el resultado
print(f'El profesor es {profesor} y el asistente es {asistente}')

