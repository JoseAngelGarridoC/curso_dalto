# Creando diccionario con dict()
diccionario = dict(nombre = 'Jose Angel', apellido = 'Garrido')
print(diccionario)
print()

# Las listas no pueden ser claves (key) y usamos frozenset para meter conjuntos
diccionario = {frozenset(['Lara', 'Caracas']):'Yaracuy'}
print(diccionario)
print()

# Creando diccionario con fromkeys()
    # Esto nos da un valor por defecto none
diccionario = dict.fromkeys(['nombre','apellido'])
print(diccionario)
print()

# Ahora, los mismo, pero cambiando el valor por 'No sé'
diccionario = dict.fromkeys(['nombre','apellido'], 'No sé')
print(diccionario)
print()

# Ejemplo de iteración de una clave (key)
diccionario = dict.fromkeys('12345','pollitos')
print(diccionario)