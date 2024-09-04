numeros = []
for i in range(6):
    numero = float(input(f"Ingrese el numero {i + 1}: "))
    numeros.append(numero)

numeros_invertidos = numeros[::-1]
print(f"El vector invertido es: {numeros_invertidos}")
