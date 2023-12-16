# For y continue
frutas = ['uvas','manzanas','peras','naranjas','bananas','kiwis']
cadena = 'Hola Madison'
numeros = [2,4,8,10]
for fruta in frutas:
    if fruta == 'naranjas':
        continue
    print(fruta)
print()    

# For y break
for fruta in frutas:
    if fruta == 'naranjas':
        break
    print(fruta)

# For iterando cada elemento de una cadena de texto
print()    
for letra in cadena:
    print(letra)

# For duplicando el valor de los elementos de una lista
print()    
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero * 2)
    # print(numeros_duplicados) => Aquí itera cada elemento formando un triángulo
print(numeros_duplicados)    
print()

# for en una sola línea de código: ¡Muy elegante!
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)