

def verificacion_ganador_perdedor (posicion_jugador)->bool:

    """
    La funcion pritea si gana, pierde o el juego termino antes de llegar a perder o a ganar
    Por parametro obtiene la posicion del jugador
    Retorna un bool
    """

    if posicion_jugador >= 30:
        print (f"¡Ganaste! La posicion a la que llegaste es {posicion_jugador + 1}")
        return True
    elif posicion_jugador == 0:
        print (f"¡Perdiste! La posicion a la que llegaste es {posicion_jugador + 1}")
        print (f"¡Suerte la proxima!")
        return True
    elif 0 < posicion_jugador < 30: 
        print (f"Juego terminado, la posicion a la que llegaste es {posicion_jugador + 1}")
        return True
    return False


def verificacion_ganador_perdedor_1 (posicion_jugador)->bool:
    
    """
    La funcion pritea si gana o pierde
    Por parametro obtiene la posicion del jugador
    Retorna un bool
    """
        
    if posicion_jugador >= 30:
        print (f"¡Ganaste! La posicion a la que llegaste es {posicion_jugador + 1}")
        return True
    elif posicion_jugador == 0:
        print (f"¡Perdiste! La posicion a la que llegaste es {posicion_jugador + 1}")
        print (f"¡Suerte la proxima!")
        return True
    return False