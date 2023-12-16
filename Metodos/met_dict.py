diccionario = {
    'name': 'Madison',
    'last_name': 'Garrido',
    'age': '2 años',
    'sex': 'femenino',
    'favorite_color': 'blue',
    'favorite_movie': 'Frozen',
}
# Con keys() nos devuelve un objeto ict_item
clave = diccionario.keys()
print(clave)

# Con get() obtengo un elemento. Si el programa no encuentra nada, el mismo continúa
valor = diccionario.get('name')
print(valor)

# Con pop() elimindo un elemento del diccionario
diccionario.pop('last_name')
print(diccionario)

# Con items() obtengo las claves con sus valores de toda la lista
dict_iterable = diccionario.items()
print(dict_iterable)

# Con clear() eliminamos toda la lista, quedando vacía
diccionario.clear()
print(diccionario)