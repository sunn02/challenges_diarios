# Ordenar Lista: Escribe un programa que ordene
# una lista de números dada por el usuario en orden ascendente.
def ordenar_lista():
    lista_usuario = [] #creo una lista usuario como vacia
    entrada = input("Inserte una lista de numeros separadas por espacio:") #Se pide al usuario 
    lista_usuario = entrada.split() #se convierte la entrada a una lista con split y se guarda en la lista usuario
    lista_usuario.sort() #ordeno con sort
    print(lista_usuario)
ordenar_lista()