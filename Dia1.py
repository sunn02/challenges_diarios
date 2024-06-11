def invertir_cadena():
    cadena_invertida = ""
    cadena = input("Ingrese una palabra:")
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida
resultado = invertir_cadena()
print(resultado)