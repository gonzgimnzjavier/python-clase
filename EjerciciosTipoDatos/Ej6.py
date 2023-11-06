
n = int(input("Introduce un número entero positivo: "))


if n <= 0:
    print("El número introducido no es positivo.")
else:
    suma = n * (n + 1) // 2
    print(f"La suma de los primeros {n} números enteros es: {suma}")
