dividendo = int(input("Introduce un dividendo: "))
divisor = int(input("Introduce un divisor: "))
if divisor == 0:
    print("No se puede dividir por 0")
else:
    cociente = dividendo / divisor
    resto = dividendo % divisor
    print(dividendo,"entre",divisor,"es",cociente,"y el resto es",resto)