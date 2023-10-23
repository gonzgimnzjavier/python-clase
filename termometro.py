temperatura=float(input("ingresa la temperatura:"))

if temperatura < 10:
    print("Nivel azul")
elif 10 <= temperatura < 20:
    print("Nivel verde")
elif 20 <= temperatura < 30:
    print("Nivel amarillo")
else:
    print("Nivel rojo")