# Los métodos son funciones específicas, por tanto, no todos los métodos son funciones

cadena1 = 'Soy Jose'
mayus = cadena1.upper()
print(mayus)
print()

cadena2 = 'Bienvenido'
minus = cadena2.lower()
print(minus)
print()

cadena3 = 'lara'
primera_mayuscula = cadena3.capitalize()
print(primera_mayuscula)
print()

cadena4 = '543576'
es_numerico = cadena4.isnumeric()
print(es_numerico)
print()

cadena5 = 'AuraCuicas'
es_alfabetico = cadena5.isalpha() # Este método no acepta espacio mi símbolos
print(es_alfabetico)
print()

cadena6 = 'Jess03Madi07'
es_alfanumerico = cadena6.isalnum()
print(es_alfanumerico)
print()

cadena7 = 'Jessika Castro Jessika Jessika'
contar_coincidencias = cadena7.count('Jessika')
print(contar_coincidencias)
print()

num_caracteres = len(cadena7) # len es una función, no un método
print(num_caracteres)
print()

busqueda_find= cadena1.find('j') # Si no hay coincidencia, devuelve -1
busqueda_index = cadena1.index('J') # Si no hay coincidencia, devuelve excepción
print(busqueda_index)
print()

cadena8 = 'Madison Garrido'
empieza_con = cadena8.startswith('M')
termina_con = cadena8.endswith('o')
reemplazar = cadena8.replace('Madi', 'Mady') # sirve para reemplar cualquier caracter de la cadena
print(empieza_con)
print(termina_con)
print(reemplazar)
print()

cadena9 = ['verde', 'morado', 'naranja']
print(cadena9[0])
print()

# Este no lo entiendo. Pendiente de investigar
cadena10 = 'amarillo azul rojo'
cadena_separada = cadena10.split(' ')
print(cadena_separada)
print()

# Ejemplo de uso del método split()
cadena = "Python es un lenguaje de programación"

# Dividir la cadena por espacios
lista = cadena.split()
print(lista) # ['Python', 'es', 'un', 'lenguaje', 'de', 'programación']
print()

# Dividir la cadena por la letra "e"
lista = cadena.split("e")
print(lista) # ['Python ', 's un l', 'nguaj', ' d', ' programación']
print()

# Dividir la cadena por espacios, pero solo una vez
lista = cadena.split(maxsplit=1)
print(lista) # ['Python', 'es un lenguaje de programación']
print()

# Ejemplo de uso del método splitlines()
cadena = """Este es un texto
que tiene varias líneas
y se puede dividir con splitlines()"""

# Dividir la cadena por saltos de línea
lista = cadena.splitlines()
print(lista) # ['Este es un texto', 'que tiene varias líneas', 'y se puede dividir con splitlines()']
print()

# Dividir la cadena por saltos de línea, pero conservando los saltos de línea
lista = cadena.splitlines(keepends=True)
print(lista) # ['Este es un texto\n', 'que tiene varias líneas\n', 'y se puede dividir con splitlines()']
print()




