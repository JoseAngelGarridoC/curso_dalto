# Definiendo una variable con camelcase: no usa el guión bajo
name_user = 'Madi'
# Definiendo una variable con snake_case: usa el guión bajo
age1 = '2' # Un número entre comillas no es un entero, es un string
age_b = ' y pronto cumplirá los 3 años'
#print(age_a)
#print(name_user)
# Concatenar con signo +
print(name_user+' tiene '+age1+ ' años'+age_b)
#del name_user
# Concatenar con función string (f'{})
print(f'{name_user} tiene {age1}años{age_b}') 

# Operadores de pertenencia in o not in => el resultado es booleano
print('pronto' in age_b)
print('casa' in age_b)
print('los' not in age_b)
print('casa' not in age_b)