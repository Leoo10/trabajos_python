buscar = 6
for numero in range(5):
    print(numero)
    if numero == buscar:
        print('encontrado', buscar)
        break
else:
    print('no pudimos encontrar tú número solicitado :(')
