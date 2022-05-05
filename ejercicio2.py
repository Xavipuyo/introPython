 # Preguntar al usuario un número y mostrar si es par o impar.
# Si el número es múltiplo de 4 imprimir el mensaje apropiado al usuario

numero = int(input('Introduzca número: '))
print('')

if numero%2 == 0:
  print('El número es par')
else:
  print('El número es impar')

if numero%4 == 0:
  print('El número es múltiplo de 4')
else:
  print('El número no es múltiplo de 4')

