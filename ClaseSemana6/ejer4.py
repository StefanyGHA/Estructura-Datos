filas = int(input("Input el numero de filas: "))
columnas = int(input("Ingresa el numero de colmnas: "))

#Crear la matriz llea con letra "A"
matriz = [["A" for _ in range(columnas)] for _ in range(filas)]

print("\nLa matriz resultante es:")
for fila in matriz:
    print(fila)

