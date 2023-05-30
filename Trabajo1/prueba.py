import random
from time import sleep


fichas = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (6, 6)]
tablero = []

humano = []
robot_1 = []
robot_2 = []
robot_3 = []

jugadores = [humano, robot_1, robot_2, robot_3]
nombres_jugadores = ["Humano", "Robot_1", "Robot_2", "Robot_3"]

# asignar fichas aleatoriamente a los cuatro jugadores
for j in range(4):
    for i in range(7):
        ficha = random.choice(fichas)
        if ficha == (6,6):
            inicial = nombres_jugadores[j]   # definir el jugador que va a empezar el juego (el que tenga la ficha 6,6)
            comienza = jugadores[j]
        fichas.remove(ficha) 
        jugadores[j].append(ficha)

print(f"El jugador que va a empezar es {inicial} con las fichas {comienza}")

# código para los turnos
indice = 0

tablero.append((6, 6))
comienza.remove((6, 6))
last_move = 'start'

def derecha():
    if tablero[-1][1] == ficha_jugar[0]:
        tablero.append(ficha_jugar)
        jugadores[i].remove(ficha_jugar)
        return True

    elif tablero[-1][1] == ficha_jugar[1]:
        f = tuple(reversed(ficha_jugar))
        tablero.append(f)
        jugadores[i].remove(ficha_jugar)
        return True
    else:
        return False

def izquierda():
            
    if tablero[0][0] == ficha_jugar[0]:
        f = tuple(reversed(ficha_jugar))
        tablero.insert(0, f)
        jugadores[i].remove(ficha_jugar)
        

    elif tablero[0][0] == ficha_jugar[1]:               
        tablero.insert(0, ficha_jugar)
        jugadores[i].remove(ficha_jugar)

def seleccion_lado():

    if tablero[0][0] == tablero[-1][1]:
        lados = ['izquierda', 'derecha']
        lado = random.choice(lados)
        if lado == 'izquierda':
            izquierda()
        else:
            derecha()
    else:
        if not derecha(): 
            izquierda()

def doble_lado(lista):
    
    repetidos = []

    for ind in range(len(lista)):
        if lista[ind][0] == primer_tablero and lista[ind][1] == primer_tablero and lista[ind] not in repetidos:
            repetidos.append(lista[ind]) 
        if lista[ind][0] == ultimo_tablero and lista[ind][1] == ultimo_tablero and lista[ind] not in repetidos:
            repetidos.append(lista[ind])
    

    if len(repetidos) == 2:
        if repetidos[0][0] == primer_tablero:
            tablero.insert(0, repetidos[0])
            jugadores[i].remove(repetidos[0])
            tablero.append(repetidos[1])
            jugadores[i].remove(repetidos[1])
        else:
            tablero.append(repetidos[0])
            jugadores[i].remove(repetidos[0])
            tablero.insert(0, repetidos[1])
            jugadores[i].remove(repetidos[1])
        return True
    else:
        return False

def doble_lado_humano(lista):
    if lista[0][0] == primer_tablero:
        tablero.insert(0, lista[0])
        jugadores[i].remove(lista[0])
        tablero.append(lista[1])
        jugadores[i].remove(lista[1])
    else:
        tablero.append(lista[0])
        jugadores[i].remove(lista[0])
        tablero.insert(0, lista[1])
        jugadores[i].remove(lista[1])     




# comienza es el nombre del jugador dque inicio
i = jugadores.index(comienza)+1
if i == 4:
    i = 0
while i < 4:

    for elem in jugadores[i]:                        # (6,6) (6,1) (1,3) 
        primer_tablero = tablero[0][0]  # Obtener el primer elemento de tablero
        ultimo_tablero = tablero[-1][1]  # Obtener el último elemento de tablero


        elementos_coincidentes = [elem for elem in jugadores[i] if ultimo_tablero in elem or primer_tablero in elem] # Filtrar los elementos de la lista que contengan el último número del último elemento de tablero o el último número del primer elemento de tablero
    
    print(f"el tablero actualizado es {tablero}")
    print(f'A Robot_1 le quedan {len(jugadores[1])} fichas')
    print(f'A Robot_2 le quedan {len(jugadores[2])} fichas')
    print(f'A Robot_3 le quedan {len(jugadores[3])} fichas')
    print(nombres_jugadores[i])
    print('fichas', jugadores[i])
    if nombres_jugadores[i] != "Humano":
        if len(elementos_coincidentes) > 0:
            print(f"Los elementos coincidentes en {nombres_jugadores[i]} son {elementos_coincidentes}")
            indexs = []
            for m in elementos_coincidentes:
                for j in range(len(jugadores[i])):
                    if jugadores[i][j] == m:
                        indexs.append(j)
            #print('index es ', indexs)
            
            # SI EL ULTIMO ELEMENTO DEL INDEXS COINCIDE CON EL ULTIMO ELEMENTO DE LA ULTIMA FICHA EN EL TABLERO SE PONE CON APPEND (A LA DERECHA)
            # SI EL PRIMER ELEMENTO DEL INDEXS COINCIDE CON EL PRIMER ELEMENTO DE LA PRIMERA FICHA EN EL TABLERO SE PONE CON INSERT (A LA IZQUIERDA)
            
            if not doble_lado(elementos_coincidentes):
                ficha_jugar = jugadores[i][random.choice(indexs)]
                print(f"la ficha a jugar es {ficha_jugar}")
                seleccion_lado()
            
            #hay que agregar las fichas de los robots al tablero y eliminarlas de las listas
        
    else:
        # parte del humano DOWN HERE
        move = 'invalid'
        while move != 'valid':
            print("los elementos coincidentes en humano son", elementos_coincidentes)
            entrada = input(f"Sus fichas son {jugadores[i]}. Escriba la posición(es) de la ficha que quiere jugar separados por coma: ").split(',')
            if len(entrada) == 2:
                try:
                    if int(entrada[0]) > len(humano) and int(entrada[1]) > len(humano):
                        indice_ok = False
                    else:
                        indice_ok = True
                except(ValueError):
                    indice_ok = False

                lista = [humano[int(entrada[0])-1], humano[int(entrada[1])-1]]

                if indice_ok == True and lista[0] in elementos_coincidentes and lista[1] in elementos_coincidentes :
                    print('fichas validas')
                    doble_lado_humano(lista)
                    move = 'valid'
                elif entrada == "pasar":
                    break
                else:
                    print('fichas invalidas, por favor selecciona una de las sugeridas')
                    move = 'invalid'
            else:
                try:
                    if int(entrada[0]) > len(humano):
                        indice_ok = False
                    else:
                        indice_ok = True
                except(ValueError):
                    indice_ok = False

                if indice_ok == True and humano[int(entrada[0])-1] in elementos_coincidentes:
                    print('ficha valida')
                    ficha_jugar = humano[int(entrada[0])-1]
                    if not doble_lado(elementos_coincidentes):
                        seleccion_lado()

                    move = 'valid'
                elif entrada[0] == "pasar":
                    break
                else:
                    print('ficha invalida, por favor selecciona una de las sugeridas')
                    move = 'invalid'

    if len(jugadores[i]) == 0:
        print('El gandor es: ', nombres_jugadores[i])
        break

    i +=1
    if i >= 4:
        i = 0
