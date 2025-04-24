welcome_message = """
    BIENVENIDO AL SISTEMA MOTOR CONTROL
    Para comenzar, debes introducir una velocidad deseada:
"""
print(welcome_message)  # Mostrar el mensaje solo una vez

while True:
    user_velocity = input("Introduce una velocidad en el rango válido (-225 a 225) o escribe STOP para detener el motor: ").strip()

    # Verificar si el usuario quiere detener el motor
    if user_velocity.upper() == "STOP":
        print("0")  # Imprimir 0 en la terminal-23
        print("El motor se ha detenido.")  # Mensaje de que el motor se ha detenido
        break  # Salir del bucle

    # Validar que la entrada sea un número
    try:
        user_velocity = int(user_velocity)
    except ValueError:
        print("Error: Debes ingresar un valor numérico. Intenta de nuevo.")
        continue  # Vuelve a pedir una entrada válida

    # Verificar el rango
    if -225 <= user_velocity <= 225:
        if user_velocity < 0:
            print(f"Velocidad establecida en {abs(user_velocity)} RPM. El motor gira hacia la izquierda.")
        elif user_velocity > 0:
            print(f"Velocidad establecida en {user_velocity} RPM. El motor gira hacia la derecha.")
        else:
            print("El motor está detenido (0 RPM).")
    else:
        print("Error: La velocidad no está en rango (-225 a 225). Intenta de nuevo.")