# Agregando un elemento a la lista
lista = ['uno', 'dos', 'lara']
print(lista)

# len() devuelve la cantidad de elementos de la lista
resultado = len(lista)
print('* La función len() contó',resultado, 'elementos')

# Agregando un elemento a la lista con .append()
lista.append('caracas')
print('* El método .append insertó caracas a la lista =>',lista)

# Agregando un elemento a la lista en un índice específico con .insert(a,b)
    # Acá no se sustituye el valor, sino, que se desplazan hacia la derecha
lista.insert(2, 3)
print('* El método .insert() agregó el 3 en el índice 2 =>',lista)

# Agregando varios elementos a la lista con .extend()
lista.extend(['Madi', 'Jess', 'Aura', 'Yo'])
print('* El método .extend() agregó varios elementos a la lista =>',lista)

#Eliminando un elemento de la lista por su índice: 
    #el primer elemento es el índice cero y contando hacia la derecha
    #y desde el último elemento sería el elemento -1 contando hacia la izquierda
lista.pop(3) # Aquí elimina el índice 3: 'lara'
lista.pop(-5) # Aquí elimina el índice -5: 'caracas'
print('* El método .pop() elimina los elementos de los índices 3 y -5 que son lara y caracas =>',lista)

# Eliminando un elemento por su valor
lista.remove('dos')
print('* El método .remove() eliminó un elemento por su valor =>',lista)

#lista.clear() #Elimina la lista completa

print()
print(lista)
print()

lista_2 = [23, 29, 22, 24, 27, 28, 21, 20, 26, 25]
# .reverse() invierte la lista, pero no la ordena.
lista_2.reverse()
print('Inviertiendo la lista sin ordenarla con .reseve() =>',lista_2)

# .sort() ordena la lista de menor a mayor
lista_2.sort()
print('* Ordenando una lista de menor a mayor con .sort() =>',lista_2)

# reverse=True ordena la lista de mayor a menor
lista_2.sort(reverse=True) 
print('* Ordenando la lista de mayor a menor con .sort() =>',lista_2)
print( )
