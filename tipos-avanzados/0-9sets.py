primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]

segundo = set(segundo)

print(primer | segundo)  # para imprimir todos los elementos del set
print(primer & segundo)  # imprime lo que esta en el primer y segundo set
# imprime lo que solamente esta en el primer set arriba que no se duplica con el más abajo.
print(primer - segundo)
print(primer ^ segundo)
