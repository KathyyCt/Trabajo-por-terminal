

def posicion_jugador (tablero:list, es_correcta:bool, posicion:int) -> int:

    mov = 1 if es_correcta else -1
    posicion += mov
    if tablero[posicion] == 1:
        posicion += mov
    elif tablero[posicion] == 2:
        posicion += mov * 2
    return posicion