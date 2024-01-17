'''
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.
'''
contraseña="contraseña"

while True:
    if input("Introduce la contraseña: ")==contraseña:
        break
print("Contraseña correcta")
