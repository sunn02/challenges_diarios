# Conversión de Temperatura: Escribe un programa que convierta una
# temperatura dada en grados Celsius a grados Fahrenheit.

def convertir_tempertura():
    temperatura_celcius = int(input("Inserte temperatura en Celcius:"))
    temperatura_fahrenheit = (temperatura_celcius * 9/5) + 32
    print(f"Grado Fahrenheit: {temperatura_fahrenheit}")
convertir_tempertura()