'''
 Creando una función que nos devuelva los números primos
 entre cero y el argumento que le pasamos
'''
# Función que verifica si un número es primo
def es_primo(num):
    # Verificamos que el número pasado no pueda dividirse
    # por ningún número entre 2 y ese mismo número - 1
    for i in range(2,num-1):
        # Si es divisible por algún número, retornamos False
        # y termina el bucle
        if num % i == 0: return False
    # Si termina el bucle, significa que no fue divisible,
    # entonces es primo
    return True

# Función que retorna una lista con todos los primos
def primos_hasta(num):
    # Creamos la lista
    primos = []
    for i in range(2,num+1):
        # Verificamos que el valor sea primo
        resultado = es_primo(i)
        # En caso de que sea lo agregamos a la lista primos = []
        if resultado == True: primos.append(i)
    return primos  # Devolvemos la lista

# Creamos el resultado llamando a la función y lo mostramos
resultado = primos_hasta(15)
print(resultado)

