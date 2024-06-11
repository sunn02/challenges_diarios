def invertir_cadena():
    cadena_invertida = ""
    cadena = input("Ingrese una palabra")
    for letra in cadena:
        cadena_invertida = letra + cadena 
    return cadena_invertida
invertir_cadena()

