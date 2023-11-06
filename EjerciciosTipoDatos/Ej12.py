precioPan = 3.49
precioPanViejo = precioPan * 0.4
cantidadPanViejoVendido = int(input("Introduce la cantidad de panes viejos vendidos: "))
print("El total de panes viejos vendidos es de: ", cantidadPanViejoVendido)
print("El precio habitual de una barra de pan es de: ", precioPan, "€","\nEl descuento que se aplica es del 60%", "\nEl total a pagar por los panes viejos es de: ", round(precioPanViejo * cantidadPanViejoVendido, 2), "€")