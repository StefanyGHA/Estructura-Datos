matriz = []

print("Ingrese los elementos de la matriz 3x3:")
for i in range(3):
    fila = []
    for j in range(3):
        elemento = float(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
        fila.append(elemento)
    matriz.append(fila)

diagonal_principal = [matriz[i][i] for i in range(3)]

print("Los elementos de la diagonal principal son:")
print(diagonal_principal)
