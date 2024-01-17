'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla
si es un número primo o no.
'''
numero=int(input("Introduce un numero entero: "))
esPrimo=True
for i in range(2,numero):
    if numero%i==0:
        esPrimo=False
        break
if esPrimo:
    print("El numero es primo")
else:
    print("El numero no es primo")
    