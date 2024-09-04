numeros = []
for i in range(5):
    numero = float(input(f"Ingrese el numero {i + 1}: "))
    numeros.append(numero)

suma = sum(numeros)
print(f"La suma de los numeros ingresados es: {suma}")
