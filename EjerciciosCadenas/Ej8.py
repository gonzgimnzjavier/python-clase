'''
Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido.
'''
precio = input("Introduce el precio del producto con dos decimales: ")
euros = precio[:precio.find(".")]
centimos = precio[precio.find(".") + 1:]
print(f"{euros} euros y {centimos} céntimos.")
