# Un programa que te dice si eres mayor o menor de edad según tu año de nacimiento:
año_nacimiento = int(input("Introduce tu año de nacimiento: "))
edad = 2023 - año_nacimiento
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Un programa que te dice si tu nombre empieza por la misma letra que tu apellido:
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
if nombre[0] == apellido[0]:
    print("Tu nombre y tu apellido empiezan por la misma letra")
else:
    print("Tu nombre y tu apellido no empiezan por la misma letra")

# Un programa que te dice si has aprobado o suspendido un examen según tu nota:
nota = float(input("Introduce tu nota: "))
if nota >= 10:
    print("Has aprobado el examen")
else:
    print("Has suspendido el examen")

# Edad para ver una peli
age = int(input())

if age >= 18:
    print('puedes ver la peli')
    
else:
    print('no puedes ver la peli')

# Intruciéndo la contraseña correcta
contraseña_guardada = 'joseph0203'
contraseña_escrita = input()

if contraseña_guardada == contraseña_escrita:
    print('Usuario_logueado')
    print('Bienvenido')
    
else:
    print('Contraseña incorrecta')
    print('Vuelva a intentarlo')

# ¿Mi sueldo me alnza para vivir?
sueldo = 1600
egresos = 2000

if sueldo >= 2500:
    print('Estas comodo en España')
    if sueldo - egresos >= 500:
        print('¡Puedes ahorrar o invertir!')  
elif sueldo > 2000 and sueldo < 2500:
    print('Estas bien, pero puedes estar mejor')
    if sueldo - egresos > 0:
        print('Vas por buen camino!')
else:
    print('¡Estas en muchos problemas!')