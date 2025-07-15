import random
from preguntas import *
from prints_preguntas import *
from tablero_casillas import *
from posicion_jugador import *
from validaciones import *
from score import * 

#preguntas de inicio de juego

nombre = input ("Ingrese su nombre: ")
verificacion_si_desea_jugar = "¿Desea jugar? (si//no): "
verificacion_si_desea_seguir = "¿Deseas seguir jugando? (si//no): "

validacion_respuesta = verificacion_preguntas (verificacion_si_desea_jugar, "si", "no")
validacion = False
if validacion_respuesta == "si":
    print ("Inicias en la posicion 15... responde correctamente para ganar.")
    validacion = True

posicion_del_jugador = 15

while validacion:

    if not indice:
        print("No hay más preguntas disponibles. Fin del juego.")
        validacion = False
    else:
        posicion_random = random.randint(0, len(indice) - 1)
        posicion = indice[posicion_random]
        indice.remove(posicion)

    pregunta_random = preguntas[posicion]
    preguntas_prints (pregunta_random)

    pregunta_respuesta = "Escribir respuesta (a//b//c): "
    verificacion_respuesta = verificacion_preguntas(pregunta_respuesta, "a", "b", "c")

    respuesta_correcta = pregunta_random["respuesta_correcta"]
    if verificacion_respuesta == respuesta_correcta:
        respuesta = True
        posicion_del_jugador = posicion_jugador(tablero, respuesta,posicion_del_jugador)
        print ("Correcto")
    else:
        respuesta = False
        posicion_del_jugador = posicion_jugador(tablero, respuesta,posicion_del_jugador)
        print ("Incorrecto")

    validacion_pregunta_seguir = verificacion_preguntas (verificacion_si_desea_seguir, "si", "no")
    
    if validacion_pregunta_seguir == "no":
        validacion = False

    posicion_jugador_validacion = validacion_ganador_perdedor (posicion_del_jugador)
    if posicion_jugador_validacion == True:
        validacion = False

    if validacion_pregunta_seguir == False:
        print("Fin del Juego")
        if 0 < posicion_del_jugador < 30:
            print (f"Juego terminado, la posicion a la que llegaste es {posicion_del_jugador}")

score (posicion_del_jugador, nombre)
