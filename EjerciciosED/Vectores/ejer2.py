numeros = []
for i in range(10):
    numero = float(input(f"Ingrese el numero {i + 1}: "))
    numeros.append(numero)

promedio = sum(numeros) / len(numeros)
print(f"El promedio de los numeros ingresados es: {promedio}")
