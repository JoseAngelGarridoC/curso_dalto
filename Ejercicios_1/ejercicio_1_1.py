# Datos
curso_dalto = 1.5
curso_corto = 2.5
curso_corto_sin_editar = 3.5
curso_promedio = 4
curso_sin_editar = 5
curso_largo = 7

print('Parte A:')
#Diferencia en porcentaje entre el curso Dalto y:
    # el mas rapido de otros cursos:
a = 100 - curso_dalto / curso_corto * 100
print(f'{a} % es la diferencia entre el curso de Dalto y el más rapido de otros cursos')

    # el mas lento de otros cursos:
b = 100 - curso_dalto / curso_largo * 100
b_1 = round(b,2)
print(f'{b_1} % es la diferencia entre el curso de Dalto y el más lento de otros cursos')

    # el promedio de los cursos:
c = 100 - curso_dalto / curso_promedio * 100
print(f'{c} % es la diferencia entre el curso de Dalto y el promedio de los cursos')
print()

print('Parte B:')
# Porcentaje de material inservible que se reduce en:
    # El promedio de los cursos
edicion_cursos_x = 100 - curso_promedio * 100 / curso_sin_editar
print(f'{edicion_cursos_x} % menos del material sin editar')

    # El curso actual
edicion_cursos_dalto = 100 - curso_dalto * 100 / curso_corto_sin_editar
d = round(edicion_cursos_dalto, 2)
print(f'{d} % menos del material sin editar')  
print()

print('Parte C:')
# Equivalencia de 10 horas del curso de Dalto respecto al promedio de otros cursos
equiv = curso_promedio * 10 / curso_dalto
e = round(equiv,2)
print(f'Ver 10 h del curso de Dalto equivalen a {e} h de otros cursos promedios')

# Equivalencia de 10 horas de otros cursos respecto al curso de Dalto
equiv_2 = curso_dalto * 10 / curso_promedio
print(f'Ver 10 h de otros cursos promedios equivalen a {equiv_2} h del curso de Dalto')