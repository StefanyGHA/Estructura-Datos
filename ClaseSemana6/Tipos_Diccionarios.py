Datos_Basicos = {"Nombres": "Juan Carlos",
                 "Apellidos":"Perez Garcia",
                 "DUI":"0102548-9",
                 "Fecha_Nacimiento":"23/7/1980",
                 "Lugar_Nacimiento":"Soya City",
                 "Nacionalidad":"Salvadoreña",
                 "Estado_civil":"Complicado"
                }

print("\nDetalle del Diccionario")    
print("===========================")    

print("\nClaves del diccionario: ",Datos_Basicos.keys())
print("\nValores del dicionario: ",Datos_Basicos.values())
print("\nElementos del diciionario: ",Datos_Basicos.items())

print("\nInscipcion del curso")
print("===========================")

print("\nDatos del participante")
print("===========================")

print("DUI:",Datos_Basicos["DUI"])
print("Nombre Completo: ",Datos_Basicos["Nombres"]+" "+Datos_Basicos["Apellidos"])
