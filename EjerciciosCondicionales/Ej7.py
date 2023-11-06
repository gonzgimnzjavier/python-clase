renta = int(input("Introduce tu renta: "))

if renta < 10000:
    print("Te corresponde un tipo impositivo del 5%")
elif renta >= 10000 and renta < 20000:
    print("Te corresponde un tipo impositivo del 15%")
elif renta >= 20000 and renta < 35000:
    print("Te corresponde un tipo impositivo del 20%")
elif renta >= 35000 and renta < 60000:
    print("Te corresponde un tipo impositivo del 30%")
else:
    print("Te corresponde un tipo impositivo del 45%")
