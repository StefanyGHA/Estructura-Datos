matriz = []
print("Ingrese los elementos de la matriz 2x3:")
for i in range(2):
    fila = []
    for j in range(3):
        elemento = float(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
        fila.append(elemento)
    matriz.append(fila)

matriz_transpuesta = [[matriz[j][i] for j in range(2)] for i in range(3)]

print("La matriz transpuesta es:")
for fila in matriz_transpuesta:
    print(fila)
