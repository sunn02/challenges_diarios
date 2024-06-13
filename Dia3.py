# DIA 3

#     Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

def contar_vocal(cadena):
    total_vocal = 0
    for a in cadena:
        if a in "aeiou":
            total_vocal += 1
    print(total_vocal)
contar_vocal("hola")