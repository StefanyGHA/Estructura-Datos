matriz = []
suma = 0

print("Ingrese los elementos de la matriz 3x3:")
for i in range(3):
    fila = []
    for j in range(3):
        elemento = float(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
        fila.append(elemento)
        suma += elemento
    matriz.append(fila)

print(f"La suma de todos los elementos de la matriz es: {suma}")
