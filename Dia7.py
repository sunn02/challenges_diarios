import random 

def juego():
    opciones = [1,2,3]
    jugador = int(input('Ingrese una opcion:\n 1.Piedra \n 2.Papel \n 3.Tijera \n'))
    computadora = random.choice(opciones)
    print(f"La computadora elige: {computadora}")

    if jugador == computadora:
        return "Empate"
    elif jugador == 1:
        if computadora == 2:
            return "Computadora gana"
        else:
            return "Ganaste"
    elif jugador == 2:
        if computadora == 3:
            return "Computadora gana"
        else:
            return "Ganaste"
    elif jugador == 3:
        if computadora == 1:
            return "Computadora gana"
        else:
            return "Ganaste"
        

resultado = juego()
print(resultado)
