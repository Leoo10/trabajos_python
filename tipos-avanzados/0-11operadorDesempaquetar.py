lista1 = [1, 2, 3, 4]

# print(lista)
# print(*lista)

lista2 = [5, 6]

combinada = [*lista1, *lista2]

print(combinada)

punto1 = {'x': 19, 'y': 'hola'}
punto2 = {'y': 15}

nuevoPunto = {**punto1, **punto2}

print(nuevoPunto)
