'''Abriendo el archivo con with open'''
with open('archivo//texto_de_jose.txt','w') as archivito:
    #Reescribimos el archivo
    #contenido = archivito.write('Madison, Jessika, Aura y Jose')
    
    
    archivito.writelines('Madi, Jess, Suegra y Jose\n')
    archivito.writelines('Marcy, Camila\n')
    archivito.writelines('Charlotte, Sharon\n')
    
    #Mostramos el archivo
    #print(contenido)
    
    '''
    Con write, reescribimos el archivo .txt dando permisos con 'w'.
    Permisos:
      * Con 'w' reescribimos el .txt
      * Con 'a' agregamos texto al .txt como si fuera .append()
    
    '''