

def verificacion_preguntas (pregunta:str, valor1:str, valor2:str, valor3:str = None):

    """
    Solicita una respuesta al usuario y valida que coincida con las opciones
    seleccionadas.

    Parametros:
    pregunta (str): Texto que se mostrara como pregunta al usuario.
    valor1 (str): Primer respuesta valida.
    valor2 (str): Segunda respuesta valida.
    valor (str, opcional): Tercera respuesta valida. Por defecto es None

    Retorna:
    str: La respuesta ingresada por el usuario que coincide con una de las opciones validas.
    """

    invalido = True
    while invalido:
        pregunta_completa = input(pregunta)
        if pregunta_completa == valor1 or pregunta_completa == valor2 or pregunta_completa == valor3:
            invalido = False
            return pregunta_completa
        else:
            print ("Error, responda correctamente")
        
    return pregunta_completa

def validacion_ganador_perdedor (posicion_del_jugador):

    """
    Verifica si el jugador ha ganado o perdido segun su pedido en el tablero.

    Parametros:
    posicion_del_jugador (int): La posicion actual del jugador.

    Retorna:
    bool: True si el jugador ha ganado (posicion 30) o perdido (posicion 0), False en cualquier otro caso.
    """

    validacion = False
    match posicion_del_jugador:
        case 30: 
            print (f"¡Ganaste! La posicion a la que llegaste es {posicion_del_jugador}")
            validacion = True
        case 0:
            print (f"¡Perdiste! La posicion a la que llegaste es {posicion_del_jugador}")
            print (f"¡Suerte la proxima!")
            validacion = True
    return validacion
