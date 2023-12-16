archivo = open('archivo//texto_de_jose.txt')
'''Lee el archivo completo'''
#print(archivo.read())

'''Lee solo una línea'''
#print(archivo.readlines(2))

'''Lee línea por línea'''
print(archivo.readline(5))

'''Cierra el archivo'''
archivo.close
