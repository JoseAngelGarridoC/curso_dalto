# Dato: 
velocidad_de_lectura = 2 # Significa 2 palabras por segundo
# Pedirle al usuario que diga cualquier texto real y:
    # Calculando cuánto tardaría en decir esa frase:
la_frase = input('Dime una frase y calcularé el tiempo que tardas en decirla: ')
    # separando las palabras de la frase con el método split(' ')
palabras_separadas = la_frase.split(' ')
#print(palabras_separadas)
    # Contamos el número de palabras con la función len()
cant_palabras = len(palabras_separadas)
    # Ahora, calculamos el tiempo que tarda el usuario en decir la frase
tiempo_en_decir_la_frase = cant_palabras / velocidad_de_lectura
print()

print('Parte A:')
print('* Tardaste', tiempo_en_decir_la_frase, 'segundos en decir la frase')
    # ¿Cuántas palabras dijo?
print('* En', tiempo_en_decir_la_frase, 'segundos dijiste', cant_palabras, 'palabras')
print()

print('Parte B:')
# Si se tarda mas de un minuto:
    # Decirle: Pará flaco. Tampoco te pedí un testamento
if tiempo_en_decir_la_frase >= 60:
    print('¡Pará flaco. Tampoco te pedí un testamento!')
else:
    print('Dijiste la frase en menos de un minuto. ¡Felicidades!')
print()
print('Parte C:')
# Dalto habla un 30% mas rapido. ¿Cuánto tardaróa en decirlo?
    # Primero calculamos la velocidad de lectura de Dalto ya que habla 30% mas rapido
lectura_dalto = velocidad_de_lectura * 130 / 100
print('La velocidad de lectura de Dalto es de', lectura_dalto, 'palabras por segundo')
    # Ahora calculamos el tiempo que tarda Dalt en leer la frase
tiempo_frase_dalto = cant_palabras / lectura_dalto
print('Por tanto, el tiempo que tarda Dalto en leer la frase es de', round(tiempo_frase_dalto,2),'segundos')
