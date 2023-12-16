# En las listas podemos cambiar los datos
lista = ["Jose", 23, True, 34.2] # Usan corchetes
lista[3] = "Jess"

# En las tuplas no se pueden cambiar los datos
tupla = ("Jose", 23, True, 34.2) # Usan paréntesis
#tupla[3] = "Jess"
print(lista)
print(lista[0])
print(tupla)

# Creando un conjunto
conjunto = {"Jose", 3, True, 5.43, True}
# En un conjunto no puede haber datos duplicados. En una lista y tupla si pueden
# haber datos duplicados
print(conjunto)
#print(conjunto[0]) # No se accede a elemetos por indice

# Creando un diccionario (dict)
diccionario = {
    'name' : 'Jose',
    'age' : 43,
    'tiene trabajo' : True,
    'es infeliz' : False   
}
print(diccionario)
print(diccionario['name'])

