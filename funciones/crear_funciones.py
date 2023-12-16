def saludar():
    print('Hola flaco, ¿Cómo vas?')
    
saludar()
saludar()
saludar()

# Creando una función con parámetros
'''print()
def saludo(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'reina'
    elif (sexo == 'hombre'):
        adjetivo = 'mano'
    else:
        adjetivo = 'amor'
    print(f'Hola {nombre}, ¿cómo estas {adjetivo}?')

saludo('Jess', 'Mujer')
saludo (nombre = input(), sexo = input())
'''
'''
# Calculando el índice de masa corporal
def imc(peso,altura):
    imc = round(peso / altura **2, 1)
    if imc < 18.5:
        resultado = 'underweight'
    if imc >= 18.5 and imc <= 24.9:
        resultado = 'Normal'
    if imc >= 25 and imc <= 29.9:
        resultado = 'Overweight'
    if imc >= 30:
        resultado = 'Obesity'
    print(f'Tu imc es {resultado}')
    
imc(float(input('Escribe tu peso: ')), float(input('Ahora, escribe tu altura: ')))'''

'''
Todo lo que coloquemos en un input() será un string. Ejm:
x = input()
print(f'El tipo de dato de x es: {type(x)}')
'''
# Creando una función que nos retorne valores
def crear_contraseña_random(num):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    #num = str(num)
    num = int(num[0])
    chars_1 = num - 1
    chars_2 = num
    chars_3 = num - 5
    contraseña = f'{chars[chars_1]}{chars[chars_2]}{chars[chars_3]}{num*2}'
    return contraseña
    
pssw = crear_contraseña_random(input())
frase = f'Tu nueva contraseña es {pssw}'
print(pssw)
# num_entero = str(num)
# num = int(num_entero[0])
'''
Todo lo que coloquemos en un input() será un string, por eso,
en este caso, debemos pasarlo a entero con int(), tal como en la línea 48.
En cambio, si colocamos un número en num (línea 55) en vez de un input(),
entonces debemos convertir dicho número a string, línea 47 => num = str(num)
'''