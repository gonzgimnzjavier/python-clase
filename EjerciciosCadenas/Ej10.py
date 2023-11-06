'''
Escribir un programa que pregunte por consola por los productos de una cesta de
la compra, separados por comas, y muestre por pantalla cada uno de los productos
en una línea distinta.
'''
cesta = input("Introduce los productos de la cesta de la compra separados por comas: ")
print(cesta.replace(",", "\n"))
