numeros = []
for i in range(7):
    numero = float(input(f"Ingrese el numero {i + 1}: "))
    numeros.append(numero)

mayor = max(numeros)
print(f"El numero mayor ingresado es: {mayor}")
