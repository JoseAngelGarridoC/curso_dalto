# Creando una función que muestre la serie fibonacci entre cero y el número dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_list = [0]
    for i in range(num):
        if b > num: return fibonacci_list
        else:
            fibonacci_list.append(b)
            a,b = b,a+b

resultado = fibonacci(55)
print(resultado)