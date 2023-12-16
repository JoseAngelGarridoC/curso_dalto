diccionario = {
    'nombre:': 'Madison',
    'apellido:': 'Garrido',
    'edad:': '2 años',
    'sexo:': 'femenino',
    'color favorito:': 'blue',
    'película favorita:': 'Frozen',
}
# Recorriendo diccionario para obtener solo los keys
for key in diccionario: 
    print(key)
print()

# Si no colacamos .items() solo generará lo keys y no sus value
for datos in diccionario.items(): 
    key = datos[0]
    value = datos [1]
    print(key,value)