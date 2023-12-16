# Creando un conjunto con set()
conjunto1 = set(['dato1'])
print(conjunto1)

# Metiendo un conjunto dentro de otro conjunto
    # Aquí utilizamos la función frozenset() para poder introducir un conjunto en otro
conjunto2 = frozenset(['dato2','dato3','dato4'])
conjunto3 = {'dato5','dato6',conjunto2}
print(conjunto3)
print()

# Verifica si es un subconjunto
conjunto4 = {8, 4, 6, 5, 2} # Super conjunto de A
conjunto5 = {8, 4, 2} # Sub conjunto de B
    # Con .issubset() comprabamos qué subconjunto es parte de otro superconjunto
#resultado1 = conjunto5.issubset(conjunto4)
    # .issubset() puede ser sutituido por <=
resultado1 = conjunto5 <= conjunto4
resultado2 = conjunto4.issubset(conjunto5)
print('* Subconjuntos')
print(resultado1) # True
print(resultado2) # False
print()

# Con .issuperset() comprabamos qué conjunto es superconjunto de un subconjunto
resultado3 = conjunto4.issuperset(conjunto5)
resultado4 = conjunto5.issuperset(conjunto4)
print('* Superconjuntos')
print(resultado3)
print(resultado4)
print()

# Verificar si hay algún número en común
    # Es True cuando no hay el subconjunto no tiene ningún elemento
    # igual a los elementos del super conjunto. Pero, si hay tan solo
    # uno igual, entonces será False
conjunto_a = {2, 4, 6, 8, 10}
conjunto_b = {1, 3, 5}
conjunto_c = {7, 8}
resultado5 = conjunto_a.isdisjoint(conjunto_b)
resultado6 = conjunto_a.isdisjoint(conjunto_c)
print('* Cuando no hay elementos iguales en ningún conjunto')
print(resultado5, '=> si no hay elementos iguales')
print(resultado6, '=> si hay tan solo un par de elementos iguales')
print()