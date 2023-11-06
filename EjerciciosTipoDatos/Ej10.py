"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un
programa que lea el número de payasos y muñecas vendidos en el último pedido y
calcule el peso total del paquete que será enviado."""


def calcular_peso_total(payasos, munecas):
    peso_payaso = 112
    peso_muneca = 75

    total_peso = (payasos * peso_payaso) + (munecas * peso_muneca)
    return total_peso


def main():
    num_payasos = int(input("Introduce el número de payasos vendidos: "))
    num_munecas = int(input("Introduce el número de muñecas vendidas: "))

    peso_total = calcular_peso_total(num_payasos, num_munecas)
    print(f"El peso total del paquete será de {peso_total} g.")


if __name__ == "__main__":
    main()


