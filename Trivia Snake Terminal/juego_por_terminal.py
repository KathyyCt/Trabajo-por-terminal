import random
import csv
from validacion_preguntas import *
from preguntas import *
from prints_preguntas import *
from tablero import *
from verificacion_ganardor_perdedor import *
from posicion_jugador import *
from validacion_posicion import *

#preguntas de inicio de juego

nombre = input ("Ingrese su nombre: ")
verificacion_si_desea_jugar = "¿Desea jugar? "
verificacion_si_desea_seguir = "¿Deseas seguir jugando?"

validacion_respuesta = verificacion_preguntas_si_no (verificacion_si_desea_jugar)
validacion = False
if validacion_respuesta == "si":
    print ("Inicias en la posicion 15... responde correctamente para ganar.")
    validacion = True


indice =[]
for i in range (len(preguntas)):
    indice.append(i)

posicion_del_jugador = 15
tablero = casillas

while validacion:

    if not indice:
        print("No hay más preguntas disponibles. Fin del juego.")
        break

    posicion_random = random.randint(0, len(indice) - 1)
    posicion = indice.pop(posicion_random)

    pregunta_random = preguntas[posicion]
    preguntas_prints (pregunta_random)

    pregunta_respuesta = "Escribir respuesta (a//b//c): "
    verificacion_respuesta = verificacion_pregunta_a_b_c(pregunta_respuesta,)

    respuesta_correcta = pregunta_random["respuesta_correcta"]
    if verificacion_respuesta == respuesta_correcta:
        respuesta = True
        posicion_del_jugador = posicion_jugador(tablero, respuesta,posicion_del_jugador)
        print ("Correcto")
    else:
        respuesta = False
        posicion_del_jugador = posicion_jugador(tablero, respuesta,posicion_del_jugador)
        print ("Incorrecto")

    validacion_pregunta_seguir = verificacion_preguntas_si_no (verificacion_si_desea_seguir)

    
    if validacion_pregunta_seguir == "no":
        break

    posicion_jugador_validacion = validacion_ganador_perdedor (posicion_del_jugador)

    if posicion_jugador_validacion == True:
        if posicion_del_jugador >= 30:
            print (f"¡Ganaste! La posicion a la que llegaste es {posicion_del_jugador}")
    
        elif posicion_del_jugador == 0:
            print (f"¡Perdiste! La posicion a la que llegaste es {posicion_del_jugador}")
            print (f"¡Suerte la proxima!")
        break

    if validacion_pregunta_seguir == False:
        print("Fin del Juego")

        if 0 < posicion_del_jugador < 30:
            print (f"Juego terminado, la posicion a la que llegaste es {posicion_del_jugador}")
        
puntaje = posicion_del_jugador
with open("Score.csv", mode="a", newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow([f"Nombre: {nombre}", f"Puntaje: {puntaje}"])


with open("Score.csv", mode="r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    print("--- PUNTAJES GUARDADOS ---\n")
    for fila in lector:
        if len(fila) == 2:
            print(f"{fila[0]} | {fila[1]}")
