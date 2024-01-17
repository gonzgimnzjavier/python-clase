'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo, de altura el número introducido.
'''
numero=int(input("Introduce un numero entero: "))
for i in range(numero):
    for j in range(i+1):
        print("*",end="")
    print("")
