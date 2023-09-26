import numpy as np
import math
import matplotlib.pyplot as plt
def simulacion_canica(dinamica,estadoIncial,clicks):
    """
    (list2D,list,int) -> list"""
    for i in range(clicks):
        matriz = np.array(dinamica)
        vector = np.array(estadoInicial)
        rest = np.dot(matriz,vector)
    return str(rest) #Retorna el estado final segun los clicks que se quieran 
#return estadoFinal
def probabilistico(dunamica,estadoInicial,clicks):   
    """ La Mtriz debe de ser doblemente estocastica para que de el estado correctamente
    (list2D,list,int) -> list"""
    for i in range(clicks):
        matriz = np.array(dinamica)
        vector = np.array(estadoInicial)
        rest = np.dot(matriz,vector)
    return str(rest) #si es que la matriz es doblemente estocastica

#return estadoFinal
def cuantico(dunamica,estadoInicial,clicks):   
    """ La Mtriz debe de contener numeros complejos para que de el estado correctamente
    (list2D,list,int) -> list"""
    for i in range(clicks):
        matriz = np.array(dinamica)
        vector = np.array(estadoInicial)
        rest = np.dot(matriz,vector)
    return str(rest) #si es que la matriz es doblemente estocastica

def grafica(estado):
    """Esta funcion recibe el estado final y lo transforma en una grafica
    (list2D) -> graphic
    """
    fig, ax = plt.subplots()
    caso = []
    for i in range(len(estado)):
        caso.append(i)
    ax.bar(caso, estado, )
    ax.set_ylabel("valores")
    ax.set_title("PROBABILIDAD")
    plt.show()
