import string
import random


def generator():
    minus = string.ascii_lowercase
    mayus = string.ascii_uppercase
    digitos = string.digits
    simbolos = string.punctuation
    characters = mayus + minus + digitos + simbolos

    password = []
    numero_char = random.randint(8,16)
    for i in range(numero_char):
        char_random = random.choice(characters)
        password.append(char_random)

    password = "".join(password)
    return password

contraseña = generator()
print(f"Tu contraseña es: {contraseña}")