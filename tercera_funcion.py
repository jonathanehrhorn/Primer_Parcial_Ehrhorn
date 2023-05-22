def ordenarCaracteres(cadena:str):
    cadena_ordenada = "".join(sorted(cadena))
    print(cadena_ordenada)

ordenarCaracteres(input("Ingrese cadena: "))