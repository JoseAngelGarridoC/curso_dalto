# El ciclo for funciona igual tanto para conjuntos como para tuplas
# Recorriendo conjuntos de string
print('* Recorriendo conjuntos de strings')
animales = {'pato','gato','perro','gallo','vaca','caballo'}
for animal in animales:
    print(f'Animales de la granja: {animal}')
print()

# Recorriendo conjuntos de números
print('* Recorriendo conjuntos de números')  
numeros = {12, 23, 34, 45, 56, 67}
for num in numeros:
    print(num * 10)
print()
    
# Recorriendo las dos conjuntos al mismo tiempo
print('* Recorriendo las dos conjuntos al mismo tiempo')
for animal,num in zip(animales,numeros):
    print(f'Recorriendo conjunto 1:{animal}')
    print(f'Redcorriendo conjunto 2:{num}')
    print()

# Recorriendo los conjuntos por rangos 
print('* Recorriendo las conjuntos por rangos')
print('Rango de 5 itemes:')
for number in range(5):
    print(number)
print()

print('* Rango desde índice inicial: 0, hasta índice final: 10')
for number_2 in range(0,10):
    print(number_2)
print()

# Forma no óptima de recorrer un conjunto por su índice
'''print('* Rango desde índice inicial: 2 hasta índice final: 6')
for number_2 in range(2,len(numeros)):
    print(numeros[number_2])
print()

print('* Rango desde índice inicial: 3 hasta índice final: 6')
for animal_2 in range(3,len(animales)):
    print(animales[animal_2])
print()'''
    
# Forma óptima de recorrer una conjunto por su índice
print('* Recorriendo conjunto con enumerate()')
for num_3 in enumerate(animales):
    indice = num_3[0]
    valor = num_3[1]
    print(f'El índice es: {indice} y su valor es: {valor}')
    
# Desafio: Desempaqueta la tupla directamente en el for. 
# Algo así como => for num,i in enumerate(numeros). 
# Es la forma más práctica y elegante
print()

# Usando else
print('* Terminando la conjunto con else')
for animal in animales:
    print(f'Ejecutándo el último bucle. Valor actual: {animal}')
else:
    print('El bucle termino')
