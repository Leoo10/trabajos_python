misDatos = [
    ['22', 3],
    ['Cuestas Manthai', 2],
    ['Leonardo', 1]
]

# nombres = []
# for midato in misDatos:
#     nombres.append(midato[0])

# print(nombres)

# nombres = [midato[0] for midato in misDatos]

# nombres = [midato for midato in misDatos if midato[1] > 1]

# nombres = [midato[0] for midato in misDatos if midato[1] > 1]

nombres = list(map(lambda midato: midato[0], misDatos))

menosMisDatos = list(filter(lambda midato: midato[1] > 2, misDatos))

print(nombres)
print(menosMisDatos)
