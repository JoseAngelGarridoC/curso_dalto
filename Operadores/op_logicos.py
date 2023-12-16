print()
resultado = True & True # Devuelve True
resultado2 = True & False # Devuelve False
resultado3 = False & True # Devuelve False
resultado4 = False & False # Devuelve False

print(f'Valores "and" devueltos: {resultado}, {resultado2}, {resultado3}, {resultado4}')
print()

resultado5 = True | True # Devuelve True
resultado6 = True | False # Devuelve True
resultado7 = False | True # Devuelve True
resultado8 = False | False # Devuelve False

print(f'Valores "or" devueltos: {resultado5}, {resultado6}, {resultado7}, {resultado8}')
print()

resultado9 = not True # Devuelve False
resultado10 = not False # Devuelve True

print(f'Valores "not" devueltos: {resultado9}, {resultado10}')
print()