def intro():
    print("\nTe encuentras en un oscuro bosque. Tienes dos caminos por delante.")
    print("El camino de la izquierda parece seguro, pero el de la derecha tiene un brillo extraño.")
    print("¿Qué camino tomarás?")
    print("1. Tomar el camino de la izquierda.")
    print("2. Tomar el camino de la derecha.")

def camino_izquierda():
    print("\nHas tomado el camino de la izquierda. Después de caminar por un rato, llegas a un claro.")
    print("En el centro del claro hay una fuente con agua cristalina.")
    print("A lo lejos, escuchas ruidos extraños en los árboles.")
    print("¿Qué harás?")
    print("1. Beber de la fuente.")
    print("2. Investigar los ruidos.")

    eleccion = input("> ")

    if eleccion == "1":
        print("\nBebes el agua de la fuente. De repente, sientes un leve mareo y caes al suelo...")
        print("Parece que el agua estaba envenenada. Has perdido.")
        fin_del_juego()
    elif eleccion == "2":
        print("\nTe acercas a los ruidos y descubres un pequeño grupo de conejos jugando entre los árboles.")
        print("Te alegras y decides regresar por el camino.")
        iniciar_juego()
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        camino_izquierda()

def camino_derecha():
    print("\nDecides tomar el camino de la derecha. A medida que avanzas, el brillo se intensifica.")
    print("Finalmente llegas a una cueva iluminada por piedras brillantes.")
    print("¿Qué harás?")
    print("1. Entrar a la cueva.")
    print("2. Volver al bosque.")

    eleccion = input("> ")

    if eleccion == "1":
        print("\nEntras en la cueva y te encuentras con un dragón guardando un gran tesoro.")
        print("El dragón te ve y te ofrece una pregunta para probar tu inteligencia.")
        print("Si respondes correctamente, podrás quedarte con parte del tesoro. Si no, el dragón te atacará.")
        print("¿Quieres intentar?")
        print("1. Aceptar el reto del dragón.")
        print("2. Huir.")

        eleccion = input("> ")

        if eleccion == "1":
            print("\nEl dragón te pregunta: '¿Cuántos meses tiene un año?'")
            respuesta = input("> ")

            if respuesta == "12":
                print("\n¡Respuesta correcta! El dragón te da una bolsa de oro.")
                ganar_juego()
            else:
                print("\nRespuesta incorrecta. El dragón te ataca y pierdes.")
                fin_del_juego()
        elif eleccion == "2":
            print("\nDecides huir de la cueva. El dragón no te persigue, pero te pierdes en el bosque.")
            print("Tras horas de caminar, encuentras un sendero hacia el pueblo.")
            print("Al llegar, te encuentras con un grupo de aventureros que te salvan.")
            ganar_juego()
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")
            camino_derecha()
    elif eleccion == "2":
        print("\nDecides volver al bosque. Después de un rato, llegas a un claro con una pequeña choza.")
        print("Parece un lugar seguro.")
        iniciar_juego()
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        camino_derecha()

def ganar_juego():
    print("\n¡Felicidades, has ganado! Has completado tu aventura con éxito.")
    jugar_otra_vez()

def fin_del_juego():
    print("\nJuego terminado. ¿Te gustaría intentarlo de nuevo?")
    jugar_otra_vez()

def jugar_otra_vez():
    print("1. Sí")
    print("2. No")

    eleccion = input("> ")

    if eleccion == "1":
        iniciar_juego()
    elif eleccion == "2":
        print("\n¡Gracias por jugar! Hasta la próxima.")
        exit()
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        jugar_otra_vez()

def iniciar_juego():
    print("\n¡Bienvenido a la aventura!")
    intro()

    eleccion = input("> ")

    if eleccion == "1":
        camino_izquierda()
    elif eleccion == "2":
        camino_derecha()
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        iniciar_juego()

# Iniciar el juego
iniciar_juego()
