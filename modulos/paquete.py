import paquete.saludar # Acá accedemos al paquete y su modulo saludar

print(paquete.saludar.saludar('Jose Angel'))
print(paquete.__path__) 
# Con el archivo __init__.py y con path puedo encontrar la ruta del archivo paquete, 
    # que literalmente es un paquete. Un paquete es un conjunto de módulos

# Para considerar que un archivo es un paquete tiene que tener el archivo __init__.py
# Por otro lado, se puede crear un sub paquete, es decir, un paquete dentro de otro paquete