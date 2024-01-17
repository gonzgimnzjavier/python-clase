'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
anual y el número de años, y muestre por pantalla el capital obtenido en la
inversión cada año que dura la inversión.
'''
cantidad=float(input("Introduce la cantidad a invertir: "))
interes=float(input("Introduce el interes anual: "))
años=int(input("Introduce el numero de años: "))
for i in range(años):
    cantidad=cantidad*(1+interes/100)
    print(f"Capital tras {i+1} años: {cantidad:.2f}")
