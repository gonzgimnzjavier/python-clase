cantidad_a_invertir=float(input("Introduce la cantidad a invertir:"))
interes_anual=float(input("Introduce el interes anual:"))
numero_de_anios=int(input("Introduce el numero de años:"))
capital_obtenido= cantidad_a_invertir*(interes_anual/100)*numero_de_anios
print("El capital obtenido es: ",capital_obtenido)