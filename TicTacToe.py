#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# tres en raya con algoritmo minimax

import sys
from operator import itemgetter

MAX = 1
MIN = -1
PROFUNDIDAD=9

global jugada_maquina

# metodo de minmax para generar las distintas opciones y seleccionar la mejor jugada 
def minimax(tablero, jugador):
    global jugada_maquina
    
    # hay ganador o tablas? (nodo terminal)
    if game_over(tablero):
        return [ganador(tablero), 0]
    
    # generar las posibles jugadas
    movimientos = []
    for jugada in range(0, len(tablero)):
        # si faltan jugadas por realizar en la posición entonces...
        if tablero[jugada] == 0:
            # creamos un tablero copia auxiliar y le asignamos el valor dependiendo del tipo de jugador (humano/ordenador)
            tableroaux = tablero[:]
            tableroaux[jugada] = jugador
            # creamos las jugadas para el jugador adversario con el nuevo valor
            puntuacion = minimax(tableroaux, jugador * (-1))
            movimientos.append([puntuacion, jugada])
    
    # si el turno es del ordenador obtenemos el movimiento con el mayor valor y si es del humano obtenemos el de menor valor 
    if jugador == MAX:
        movimiento = max(movimientos, key=str)        
        jugada_maquina = movimiento[1]
        return movimiento 
    else:       
        movimiento = min(movimientos, key=str)        
        return movimiento[0]
    
    #Tomamos en cuenta el # de casillas disponibles
def minmaxNivel2(tablero, jugador, profundidad ):
    global jugada_Maquina
    
    #Le asignamos valor a la jugada dependiendo el tipo de jugador
    if juador== MAX:
        movimiento=[-1,-1,-infinity]
    else:
        movimiento=[-1,-1,+infinity]
        
        # // Si se acabo el juego o llegamos al maximo de profundidad
    if profundidad ==0 or game_over(tablero):
        return [ganador(tablero), 0]
    
   # hacemos llamado al min max de manera recursiva
    
    for jugada in range(0,len(tablero)):
        
        #Se guarda el indice de la fila y la columna
        x,y=jugada[0],jugada[1]
        
        tablero[x][y]=jugador
        puntaje= minmaxNivel1(tablero, jugador * (-1), profundidad-1 )
        tablero[x][y]=0
        puntaje[0],puntaje[1]=x,y
        
        
        if jugador==MAX:
            if puntaje[2]>movimiento[2]
                movimiento=puntaje
        else:
            if puntaje[2]<movimiento[2]
                movimiento=puntaje
    
    return movimiento
   
def game_over(tablero):
    # hay tablas?
    no_tablas = False
    for i in range(0, len(tablero)):
        if tablero[i] == 0:
            no_tablas = True
            
    # hay ganador?
    if ganador(tablero) == 0 and no_tablas:
        return False
    else:
        return True

    
def ganador(tablero):
    # combinaciones de estados de ganadores
    lineas = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5,8], [0, 4, 8], [2, 4, 6]]
    ganador = 0
    for linea in lineas:
        if tablero[linea[0]] == tablero[linea[1]] and tablero[linea[0]] == tablero[linea[2]] and tablero[linea[0]] != 0:
            ganador = tablero[linea[0]]
    return ganador

# metodo que imprime el trablero de juego 
def ver_tablero(tablero):
    
    board = list(map(str, tablero))    
    for i in range(0, len(tablero)):
        if tablero[i] == MAX:
            board[i] = 'X'
        elif tablero[i] == MIN:
            board[i] = 'O'
        else:
            board[i] = ' '
  
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')    

# metodo encargado de procesar el movimiento del jugador humano
def juega_humano(tablero):
    ok= False
    while not ok:
        casilla = input("Casilla?")
        # obtenemos la posición de la casilla de 1-9 y comparamos con su respectivo indice en la lista
        if str(casilla) in '0123456789' and len(str(casilla)) == 1 and tablero[int(casilla)-1] == 0:
            # asignamos a la casilla del jugador un valor de -1
            tablero[int(casilla)-1] = MIN
            ok = True
        if casilla == "exit":
            sys.exit(0)
    return tablero

# metodo del ordenador donde se aplica min-max con la propagación y selección de la mejor opción de la jugada teniendo la función de evaluación
def juega_ordenadorNive1(tablero):
    global jugada_maquina
    punt = minimax(tablero[:], MAX)
    tablero[jugada_maquina] = MAX
    return tablero

def juega_ordenadorNiveL2(tablero):
    global jugada_maquina
    punt = minmaxNivel2(tablero[:], MAX, PROFUNDIDAD)
    print(punt)
    tablero[jugada_maquina] = MAX
    return tablero


def incia_Humano(tablero):
    while(True):
        ver_tablero(tablero)
        tablero = juega_humano(tablero)
        if game_over(tablero):
            break
        
        tablero = juega_ordenadorNive1(tablero)
        if game_over(tablero):
            break
    
def inicia_Ordenador(tablero):
     while(True):
        ver_tablero(tablero)
        tablero = juega_ordenadorNiveL2(tablero)
        if game_over(tablero):
            break
        
        tablero = juega_humano(tablero)
        if game_over(tablero):
            break


if __name__ == "__main__":
    print("Seleccione un nivel de dificultad" +" 1 ó 2")
    print("Introduce casilla o exit para terminar")
    tablero = [0,0,0,0,0,0,0,0,0]
    inicio=input("Dificultad?")
    #obtenemos el nivel de dificultad 
    if(inicio==1):
        inicia_Humano(tablero)
    
    else:
        inicia_Ordenador(tablero)
    
            
    ver_tablero(tablero)
    g = ganador(tablero)
    if g == 0:
        gana = "Tablas"
    elif g == MIN:
        gana = "Jugador"
    else:
        gana = "Ordenador"
    
    print("Ganador: " + gana)
 


# In[ ]:




