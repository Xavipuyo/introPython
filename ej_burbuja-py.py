# lista = [72, 100, 51, 13, 40]
# # Necesario como verdadero (True) para ingresar al bucle while
# intercambio = True

# while intercambio:
#   intercambio = False # no hay intercambios hasta ahora
#   for i in range(len(lista) - 1):
#     if lista[i] > lista[i + 1]:
#       intercambio = True # se intercambian
#       lista[i], lista[i + 1] = lista[i + 1], lista[i]

# print(lista)

# # Método sort() ordena las listas
# lista = [72, 100, 51, 13, 40]
# lista.sort()

# print(lista)

# # Método reverse() invierte el orden de la lista
# lista = [72, 100, 51, 13, 40]
# print(lista)
# lista.reverse()

# print(lista)

lista = [72, 100, 51, 13, 40]
lista_2 = lista
lista[0] = 2
print(lista_2)
print(lista)

lista = ["x", "y", 1, 2, 3]
print("x" in lista)
print("z" not in lista)
print(2 not in lista)