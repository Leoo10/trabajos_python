clientes = ['Juan solis', 'Soledad cagnolo', 'julieta strasorier']
turnos = ['26/10/2023', '21/11/2023', '14/09/2023', '13/09/2023']
reservas = {}
clave = -1
elemento = -1


for i in range(len(clientes)):
    reservas[clientes[elemento]] = turnos[clave]
    clave -= 1
    elemento += 1
print(reservas)
