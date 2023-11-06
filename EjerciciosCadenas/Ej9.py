'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
anterior para que también funcione cuando el día o el mes se introduzcan con un
solo carácter.
'''
fecha = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
dia = fecha[:fecha.find("/")]
mes = fecha[fecha.find("/") + 1:fecha.rfind("/")]
año = fecha[fecha.rfind("/") + 1:]
print(f"Tu fecha de nacimiento es el {dia} de {mes} de {año}.")
