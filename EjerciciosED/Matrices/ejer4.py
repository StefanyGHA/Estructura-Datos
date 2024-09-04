matriz1 = []
matriz2 = []

print("Ingrese los elementos de la primera matriz 2x2:")
for i in range(2):
    fila = []
    for j in range(2):
        elemento = float(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
        fila.append(elemento)
    matriz1.append(fila)

print("Ingrese los elementos de la segunda matriz 2x2:")
for i in range(2):
    fila = []
    for j in range(2):
        elemento = float(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
        fila.append(elemento)
    matriz2.append(fila)

resultado = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            resultado[i][j] += matriz1[i][k] * matriz2[k][j]

print("El resultado de la multiplicacion de las dos matrices es:")
for fila in resultado:
    print(fila)
