def sumar_valores(a,b,c):
    return a+b+c
resultado = sumar_valores(2,3,9)
print(resultado)

# Forma no optima de sumar valores
'''
def suma(lista):
    numeros_sum = 0
    for numero in lista:
        numeros_sum = numeros_sum + numero
    return numeros_sum

total = suma([1,2,3,4,5,6,7])
print(total)'''

# Acá dos formas de hacerlo usando el operador * como
    # argumento (*args) y otra sin este operador
def suma(*numero):
    return sum(numero)

total = suma(1,2,3,4,5,6,7)
print(total)

def suma(lista):
    return sum(*[lista])

total = suma([1,2,3,4,5,6,7])
print(total)