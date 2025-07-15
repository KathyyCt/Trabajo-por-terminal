
def preguntas_prints (lista_posicion:dict):

    """
    Muestra por pantalla una pregunta junto con sus posibles respuestas.

    Parametros:
    lista_posicion (dict): diccionario que contiene la pregunta y sus tres opciones
    de respuesta.
    Debe tener las claves: "pregunta", "respuesta_a", "respuesta_b", "respuesta_c".

    Retorno:
    Ninguno
    """

    print("\n" + lista_posicion["pregunta"])
    print(lista_posicion["respuesta_a"])
    print(lista_posicion["respuesta_b"])
    print(lista_posicion["respuesta_c"])
