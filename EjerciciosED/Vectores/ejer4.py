numeros = []
positivos = 0

for i in range(8):
    numero = float(input(f"Ingrese el numero {i + 1}: "))
    numeros.append(numero)
    if numero > 0:
        positivos += 1

print(f"Se ingresaron {positivos} numeros positivos.")
