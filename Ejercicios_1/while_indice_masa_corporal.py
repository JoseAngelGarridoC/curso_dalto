# Calculando el índice de masa corporal
m = float(input('Escribe tu peso: '))
h = float(input('Ahora, escribe tu altura: '))
imc = round(m / h **2, 1)

if imc < 18.5:
    print('Underweight')
if imc >= 18.5 and imc <= 24.9:
    print('Normal')
if imc >= 25 and imc <= 29.9:
    print('Overweight')
if imc >= 30:
    print('Obesity')
#print(imc)