puntuacion = float(input("Introduce tu puntuacion: "))
dinero = 2400
if puntuacion == 0.0:
    print("Tu nivel de rendimiento es innaceptable")
    print("Tu puntuacion es: ", puntuacion)
    print("Tu dinero es: ", "{:.2f}".format(dinero*puntuacion))
elif puntuacion == 0.4:
    print("Tu nivel de rendimiento es aceptable")
    print("Tu puntuacion es: ", puntuacion)
    print("Tu dinero es: ", "{:.2f}".format(dinero*puntuacion))
elif puntuacion >= 0.6:
    print("Tu nivel de rendimiento es meritorio")
    print("Tu puntuacion es: ", puntuacion)
    print("Tu dinero es: ", "{:.2f}".format(dinero*puntuacion))

