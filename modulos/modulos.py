from modulo_saludar import saludar as saludito, saludar_star_wars as saludo_es
#import modulo_saludar as m_saludar
from modulo_mando.saludo_mandaloriano import saludar as hola_mando # Acá importamos la función desde una carpeta 

saludo = saludito('Jose Angel')
saludo_star_wars = saludo_es('Anakin')
saludo_mando = hola_mando('Mando')

print(saludo)
print(saludo_star_wars)
print(saludo_mando)

#print(m_saludar.__name__) # Muestra el nombre del módulo que estamos importando