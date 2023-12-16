# desempaquetado de datos en tuplas
datos_mujer = ('Jessika','Castro', 38)
nombre,apellido,edad = datos_mujer
print(nombre)
print(apellido)
print(edad)
print()
# desempaquetado de datos en listas
datos_hombre = ['Jose','Garrido',43]
nombre,apellido,edad = datos_hombre
print(nombre)
print(apellido)
print(edad)
print()

# Ejemplo de un pedido de cliente:
datos_cliente = ('Aura','Cuicas','reloj','Vía Complutense, 87, 4CI','12 de noviembre del 2023')
nombre,apellido,articulo,direccion,fecha_de_entrega = datos_cliente
print('Nombre del cliente:',nombre,apellido)
print('Articulo:',articulo)
print('dirección de entrega:',direccion)
print('Fecha de entrega:',fecha_de_entrega)