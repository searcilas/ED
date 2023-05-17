import random

fichas = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (6, 6)]

humano = []
robot_1 = []
robot_2 = []
robot_3 = []

jugadores = [humano, robot_1, robot_2, robot_3]
nombres_jugadores = ["humano", "robot_1", "robot_2", "robot_3"]

for j in range(4):
    for i in range(7):
        ficha = random.choice(fichas)
        if ficha == (6,6):
            inicial = nombres_jugadores[j]   # definir el jugador que va a empezar el juego (el que tenga la ficha 6,6)
        fichas.remove(ficha) 
        jugadores[j].append(ficha)


# print(f"Las fichas de humano son {humano}. Su tamaño debería ser 7 pero su tamaño es {len(humano)}")
# print(robot_1)
# print(robot_2)

print(jugadores)
print(f"El jugador que va a empezar es {inicial}")

