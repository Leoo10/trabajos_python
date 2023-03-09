punto = {
    'x': 25, 'y': 50
}

# print(punto['x'])
# print(punto['y'])

# print(punto.get('y', 97))

del punto['x']

# print(punto)
punto['x'] = 25

for valores in punto:
    print(valores, punto[valores])

for llave, valores in punto.items():
    print(llave, valores)


usuarios = [
    {'id': 1, 'Nombre': 'Chanchito'},
    {'id': 2, 'Nombre': 'Feliz'},
    {'id': 3, 'Nombre': 'Nicolas'},
    {'id': 4, 'Nombre': 'Felipe'}
]

for usuario in usuarios:
    print(usuario['Nombre'])
