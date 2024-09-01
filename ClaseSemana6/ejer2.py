#Fechas de actividades
fechas_actividades = [
    "Fecha de inscripcion: 01-07-24",
    "Fecha de inicio de ciclo 2: 15-06-24",
    "Fecha de finalizacion: 15-12-24"
]

#Funcion para interactuar con el chatbot
def chatbot_respuesta(pregunta):
    if "inscripcion" in pregunta.lower():
        return f"La {fechas_actividades[0]}"
    elif "inicio" in pregunta.lower():
        return f"La {fechas_actividades[1]}"
    elif "finalizacion" in pregunta.lower() or "final" in pregunta.lower():
        return f"La {fechas_actividades[2]}"
    else:
        return "Lo siento, no entiendo tu pregunta. Por favor, pregunta sobre la fecha de inscripcin, inicio de ciclo o finalizacion."

#Mostrar las opciones al usuario
print("¡Hola!. Soy tu asistente virtual UNIVO. Puedo ayudarte a encontrar las fechas importantes de la universidad.")
print("Puedes preguntarme sobre la fecha de inscripcion, inicio o finalizacion del ciclo 02.")

#Solicitar al usuario que seleccione una opcion o hable con el chatbot
while True:
    opcion = input("\n¿Como puedo ayudarte? (Escribe tu pregunta o escribe 'salir' para finalizar el chat): ").strip().lower()

    if opcion == "salir":
        print("Cerrando el programa.......")
        break
    else:
        respuesta = chatbot_respuesta(opcion)
        print(f"\n{respuesta}")
