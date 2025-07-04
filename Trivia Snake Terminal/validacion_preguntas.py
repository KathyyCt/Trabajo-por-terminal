

def verificacion_preguntas_si_no (pregunta:str):

    """
    La funcion lo que hace es validar si se responde correctamente con si o no una pregunta
    Por parametro recibe una pregunta (str)
    Retorna un bool
    """

    invalido = True
    while invalido:
        pregunta_completa = input(pregunta + "(si//no): ")
        if pregunta_completa == "si" or pregunta_completa == "no":
            invalido = False
            return pregunta_completa
        else:
            print ("Error, responda correctamente")

def verificacion_pregunta_a_b_c (pregunta:str)-> str:

    """
    La funcion lo que hace es validar si se responde correctamente con a//b//c una pregunta
    Por parametro recibe una pregunta (str)
    Retorna un string (a//b//c)
    """
        
    invalido = True
    while invalido:
        pregunta_completa = input(pregunta)
        if pregunta_completa == "a" or pregunta_completa == "b" or pregunta_completa == "c":
            invalido = False
            return pregunta_completa
        else:
            print("Error, responde con a, b o c")
