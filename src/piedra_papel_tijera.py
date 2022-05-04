'''NAME
piedra_papel_tijera.py
VERSION
1.0
AUTHOR
Andres Rivera Ramirez.

CATEGORY
Game

DESCRIPTION
Juego de piedra papel o tijera con generador de numeros random y 
estructuras if dentro de un ciclo while.
CATEGORY

USAGE
py src/piedra_papel_tijera.py
ARGUMENTS
None
SEE ALSO


'''
import random

# Guardar las opciones validas

movimientos_posibles = ["roca", "papel", "tijera"]
nombre_usuario = input("Introduzca su nombre:")

# El juego esta en un ciclo while para jugar mas de una vez
while True:
    # Pedir su opcion al usuario
    movimiento_jugador = input(
        "Inserte su movimiento (roca, papel o tijera):").lower()
    if(not(movimiento_jugador in movimientos_posibles)):
        print("Introduzca un movimiento valido")
        continue
        # Declarar mensajes de victoria y derrota
        
    mensaje_v = f"Ganaste {nombre_usuario}"
    mensaje_d = "La computadora gana..."
    
    # Obtener la opcion de la computadora
    movimiento_computadora = random.choice(movimientos_posibles)
    
    # Comparar la opcion del usuario con la de la computadora
    # Si la opcion del usuario es igual de la computadora se declara empate
    if(movimiento_jugador == movimiento_computadora):
        print("¡Empate!")
        # Si la opcion del usuario es roca:
        
    elif(movimiento_jugador == "roca"):
        if(movimiento_computadora == "papel"):
            print(mensaje_d)
        else:
            print(mensaje_v)
            # Si la opcion del usuario es papel
            
    elif(movimiento_jugador == "papel"):
        if(movimiento_computadora == "tijera"):
            print(mensaje_d)
        else:
            print(mensaje_v)
            
    else:
        # Si la opcion del usuario es tijeras
        if(movimiento_computadora == "roca"):
            print(mensaje_d)
        else:
            print(mensaje_v)
         # Se detiene el programa si se han jugado 100 partidas
        if(i >= 100):
            raise ValueError("Creo que hemos jugado demasiado, descansa")
            
            # Se pregunta si se jugara otra vez, sino se rommpe el ciclo while
    jugar_de_nuevo = input("¿Quieres jugar de nuevo?\ny/n\n")
    if(jugar_de_nuevo.lower() != "y"):
        break
