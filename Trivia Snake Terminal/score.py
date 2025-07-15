
import csv

def score (puntaje:int,nombre:str):

    """
    Guarda el nombre y puntaje (posicion del jugador) en un archivo csv.

    Parametros:
    Nombre (str): Nombre del jugador
    Puntaje (int): Puntaje obtenido.

    Retorno:
    Nunguno
    """

    with open("Score.csv", mode="a", newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([f"Nombre: {nombre}", f"Puntaje: {puntaje}"])

    with open("Score.csv", mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        print("--- PUNTAJES GUARDADOS ---\n")
        for fila in lector:
            if len(fila) == 2:
                print(f"{fila[0]} | {fila[1]}")
