# Atividade POO 

# 1 QUESTÃO

lista_notas = []

while True:
    valores = float(input("Digite uma nota: (Digite -1 para encerrar:)"))
    if valores != (-1):
        lista_notas.append(valores)
    else:
        break

print(lista_notas)

# A

print(f"Esta lista tem {len(lista_notas)} notas.")

#  B

print(lista_notas)

# C

for nota in reversed (lista_notas):
    print(nota)

#  D

print(sum(lista_notas))

#  E

print(sum(lista_notas) / len(lista_notas))

# F
quantidade = 0
for nota in lista_notas:
    if nota > (sum(lista_notas) / len(lista_notas)):
        quantidade += 1
print(f"notas acima da média: {quantidade}")

#  G

quantidade = 0
for nota in lista_notas:
    if nota < 7:
        quantidade += 1
print(f"notas abaixo de 7: {quantidade}")

#  H

print("EU AMO POO.")





