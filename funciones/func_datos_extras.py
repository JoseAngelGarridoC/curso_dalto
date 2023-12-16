def info(nombre, apellido, oficio, edad):
    return f'Nombre: {nombre}, apellido: {apellido}, edad: {edad} y oficio: {oficio}'

datos = info(edad = 43, apellido = 'Garrido', nombre = 'Jose Angel', oficio ='Programador')
print(datos)

'''
colores = ['amarillo','azul','rojo']
def lista(colores):
    
    colores = colores.insert(0,colores)
    return colores
mis_colors = lista('azul')
print(mis_colors)
'''

def potencia(x):
    return x**2

resultado = potencia(2)
print(resultado)
    