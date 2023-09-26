# De lo clasico a lo cuantico

Esta librería proporciona funciones para realizar experimentos cuánticos básicos relacionados con el comportamiento de canicas en cajas y estados probabilísticos en sistemas cuánticos.

## Funciones Disponibles

### simulacion_canica(dinamica, estadoInicial, clicks)
```python
def simulacion_canica(dinamica,estadoIncial,clicks):
    for i in range(clicks):
        matriz = np.array(dinamica)
        vector = np.array(estadoInicial)
        rest = np.dot(matriz,vector)
    return str(rest) 
```

Esta función simula el movimiento de canicas en cajas a lo largo de una serie de "clicks" utilizando una matriz de dinámica dada y un estado inicial. Retorna el estado final después de la simulación.

**Parámetros:**

- `dinamica` (list2D): Una lista 2D que representa la matriz de dinámica del sistema.
- `estadoInicial` (list): Una lista que representa el estado inicial del sistema.
- `clicks` (int): El número de "clicks" o pasos en la simulación.

**Retorno:**

- Una lista que representa el estado final después de la simulación.

### probabilistico(dinamica, estadoInicial, clicks)
```python

def probabilistico(dunamica,estadoInicial,clicks):   

    for i in range(clicks):
        matriz = np.array(dinamica)
        vector = np.array(estadoInicial)
        rest = np.dot(matriz,vector)
    return str(rest)
```

Esta función calcula el estado probabilístico después de una serie de "clicks" utilizando una matriz de dinámica que debe ser doblemente estocástica y un estado inicial.

**Parámetros:**

- `dinamica` (list2D): Una lista 2D que representa la matriz de dinámica del sistema (debe ser doblemente estocástica).
- `estadoInicial` (list): Una lista que representa el estado inicial del sistema.
- `clicks` (int): El número de "clicks" o pasos en la simulación.

**Retorno:**

- Una lista que representa el estado final después de la simulación.

### cuantico(dinamica, estadoInicial, clicks)

```python
def cuantico(dunamica,estadoInicial,clicks):   
    for i in range(clicks):
        matriz = np.array(dinamica)
        vector = np.array(estadoInicial)
        rest = np.dot(matriz,vector)
    return str(rest)
```
Esta función calcula el estado cuántico después de una serie de "clicks" utilizando una matriz de dinámica que puede contener números complejos y un estado inicial.

**Parámetros:**

- `dinamica` (list2D): Una lista 2D que representa la matriz de dinámica del sistema (puede contener números complejos).
- `estadoInicial` (list): Una lista que representa el estado inicial del sistema.
- `clicks` (int): El número de "clicks" o pasos en la simulación.

**Retorno:**

- Una lista que representa el estado final después de la simulación.

### grafica(estado)
```python
def grafica(estado):
    fig, ax = plt.subplots()
    caso = []
    for i in range(len(estado)):
        caso.append(i)
    ax.bar(caso, estado, )
    ax.set_ylabel("valores")
    ax.set_title("PROBABILIDAD")
    plt.show()
```

Esta función recibe el estado final de un sistema y lo representa en un gráfico de barras para visualizar la probabilidad de cada estado.

**Parámetros:**

- `estado` (list2D): Una lista que representa el estado final del sistema.

**Retorno:**

- Una gráfica de barras que muestra la probabilidad de cada estado en el sistema.


