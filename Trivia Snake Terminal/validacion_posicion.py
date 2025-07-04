

def validacion_ganador_perdedor (posicion_del_jugador):
        
    validacion = False
    if posicion_del_jugador >= 30 or posicion_del_jugador == 0:
        validacion = True

    return validacion