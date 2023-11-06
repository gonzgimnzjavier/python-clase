dinero_depositado = float(input("Cuanto dinero depositado: "))
interes_anual = 0.04
año1 = dinero_depositado * (1 + interes_anual)
año2 = dinero_depositado * (1 + interes_anual) ** 2
año3 = dinero_depositado * (1 + interes_anual) ** 3
print("El valor de año 1 es: ", año1)
print("El valor de año 2 es: ", año2)
print("El valor de año 3 es: ", año3)