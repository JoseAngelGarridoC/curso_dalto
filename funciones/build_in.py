# Las funciones build in son funciones integradas en python

# Encontrando el máximo y el mínimo
numeros = [2,5,78,34]

num_max = max(numeros)
num_min = min(numeros)
print(num_max)
print(num_min)

# Redondeo a dos decimales
numero = round(3.141592 , 2)
print(numero)

# Retorna false si la instancia es 0, datos vacíos, False, None
# Retorna true si la instancia es distinto a 0, True, cadena, datos no vacíos
resultado_bool = bool(None)
print(resultado_bool)

# Retorna true si todos los valores son verdaderos
resultado_all = all([True, 23, [3,4,5], 'hola']) # Si hay un valor false, el resultado será false
print(resultado_all)

total = sum(numeros)
print(total)