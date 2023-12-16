'''Abriendo el archivo con with open'''
with open('archivo//texto_de_jose.txt') as archivito:
    #Leemos el archivo
    contenido = archivito.read()
    
    #Mostramos el archivo
    print(contenido)
    
    '''No es necesario cerrarlo cuando se una with open'''