pizza_vegetaria = input("¿Pizza vegetariana? (s/n): ").lower()
ingredientes_vegetarianos = ["tofu","pimiento"]
ingredientes_no_vegetarianos = ["peperoni","salmon","jamon"]
ingredientes_comunes = ["mozarella","tomate"]
pizza_cliente = []
if pizza_vegetaria == "s":
    print("Has elegido Pizza vegetariana")
    print("Ingredientes: ", ingredientes_vegetarianos+ingredientes_comunes)
    decision=input("Elija entre Tofu o Pimiento:").lower()
    if decision == "tofu":
        pizza_cliente.append("Tofu")
        pizza_cliente +=ingredientes_comunes
        print("La pizza es vegetariana y sus ingredientes son: ", pizza_cliente)
    elif decision == "pimiento":
        pizza_cliente.append("Pimiento")
        pizza_cliente +=ingredientes_comunes
        print("La pizza es vegetariana y sus ingredientes son: ", pizza_cliente)
    else:
        print("ERROR")
else:
    print("Pizza no vegetariana")
    print("Ingredientes: ", ingredientes_no_vegetarianos+ ingredientes_comunes)
    decision=input("Elija entre Peperoni, Salmon o Jamon:").lower()
    if decision == "peperoni":
        pizza_cliente.append("Peperoni")
        pizza_cliente +=ingredientes_comunes
        print("La pizza es no vegetariana y sus ingredientes son: ", pizza_cliente)
    elif decision == "salmon":
        pizza_cliente.append("Salmon")
        pizza_cliente +=ingredientes_comunes
        print("La pizza es no vegetariana y sus ingredientes son: ", pizza_cliente)
    elif decision == "jamon":
        pizza_cliente.append("Jamon")
        pizza_cliente +=ingredientes_comunes
        print("La pizza es no vegetariana y sus ingredientes son: ", pizza_cliente)
    else:
        print("ERROR")