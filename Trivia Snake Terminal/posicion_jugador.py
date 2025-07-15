

def posicion_jugador (tablero:list, es_correcta:bool, posicion:int) -> int:

    """
    Actualiza la posicion del jugador en el tablero segun si la respuesta es correcta
    o incorrecta. tambien interpreta casillas especiales que modifican el movimiento.

    Parametros:
    tablero (list): lista de enteros que representa el tableto. Cada casilla puede tener:
        - 0: sin efecto
        - un numero > 0: casilla especial que avanza segun el numero.
        - un numero < 0: casillas especial que retrocede segunn el numero.
    es_correcta (bool): indica si es correcta (True) o incorrecta (False)
    posicion (int): numero que representa la posicion actual del jugador en el tablero.

    Retorna:
    int: Nueva posicion del jugador despues del movimiento.
    """
    if es_correcta:
        mov = 1
    else:
        mov = -1

    posicion += mov
    if tablero[posicion] != 0:
        posicion += mov * tablero[posicion]
        
    return posicion
