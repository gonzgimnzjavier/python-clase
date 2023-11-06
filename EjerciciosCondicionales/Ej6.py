#Coleccion de caracteres validos
caracteres_validos1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
caracteres_validos2 = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
sexo=input("Introduce tu sexo: ").lower()
nombre=input("Introduce tu nombre: ").lower()
#se verifica el primer caracter hasta la n
if (nombre[0] in caracteres_validos1 and sexo=="femenino") or (nombre[0] in caracteres_validos2 and sexo=="masculino"):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")

