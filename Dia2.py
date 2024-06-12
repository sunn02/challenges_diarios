#Tabla de Multiplicar: Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.

def tabla():
    numero = int(input("Introduzca un numero:"))
    for i in range(1,11):
        multiplicacion = i * numero 
        resultado = (f"{numero} x {i} = {multiplicacion}")
        print(resultado)
tabla()
