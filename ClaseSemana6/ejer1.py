temperaturas = []
print("Por favor, ingresa 10 temperaturas:")

for i in range(10):

    temperatura = float(input(f"Temperatura {i + 1}: "))
    temperaturas.append(temperaturas)

promedio = sum(temperaturas) / len/(temperaturas)    

print(f"\nEl promedio de las temperaturase es: {promedio:.2f}")


while True:
    opcion = input("\¿Ver alguna temperatura especifica? (si/no): ").strip().lower()

    if opcion == "si":

        posicion = int(input("Ingresa la posicion (1-10) de la temperatura que deseas ver: "))
        if 1 <= posicion <= 10:
            print(f"La temperatura en la posicion {posicion} es: {temperatura[posicion - 1]:.2f}")
        else:
            print("posicion fuera de rango. Por favor ingresa um numero entre 1 y 10.")

    elif opcion == "no":
        print("Cierre del programa.")  
        break

    else:
        print("Por favor, ingresa 'si' o 'no'.")      
