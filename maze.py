import time
#@author: Sergio paramo
#@description: laberinto
#@date: 10-05-2020
def Inicio(position):
    for i in range(9):
        print(laberinto[i])
    print("\n")

    time.sleep(2)

    if(laberinto[position[0]][position[1] + 1] == " "):
        move([position[0],position[1] + 1], position)
    elif(laberinto[position[0] + 1][position[1]] == " "):
        move([position[0] + 1,position[1]], position)

def move(posicion, ultimaPosicion):
    laberinto[ultimaPosicion[0]][ultimaPosicion[1]] = "|";

    for i in range(9):
        print(laberinto[i])
    print("\n")

    time.sleep(0.5)

    if(ultimaPosicion[0] == posicion[0] and ultimaPosicion[1] == posicion[1] - 1):
        if(posicion[1] == 9 or laberinto[posicion[0]][posicion[1] + 1] != " "):
            if (posicion[0] == 0 or laberinto[posicion[0] - 1][posicion[1]] != " "):
                if (posicion[0] == 9 or laberinto[posicion[0] + 1][posicion[1]] != " "):
                    print("Fin del laberinto!")
                else: move([posicion[0] + 1, posicion[1]], posicion)
            else: move([posicion[0] - 1, posicion[1]], posicion)
        else: move([posicion[0], posicion[1] + 1], posicion)

    elif (ultimaPosicion[0] == posicion[0] and ultimaPosicion[1] == posicion[1] + 1):
        if (posicion[1] == 0 or laberinto[posicion[0]][posicion[1] - 1] != " "):
            if (posicion[0] == 0 or laberinto[posicion[0] - 1][posicion[1]] != " "):
                if (posicion[0] == 9 or laberinto[posicion[0] + 1][posicion[1]] != " "):
                    print("Fin del laberinto!")
                else: move([posicion[0] + 1, posicion[1]], posicion)
            else: move([posicion[0] - 1, posicion[1]], posicion)
        else: move([posicion[0], posicion[1] - 1], posicion)

    elif (ultimaPosicion[0] == posicion[0] - 1 and ultimaPosicion[1] == posicion[1]):
        if (posicion[0] == 9 or laberinto[posicion[0] + 1][posicion[1]] != " "):
            if(posicion[1] == 9 or laberinto[posicion[0]][posicion[1] + 1] != " "):
                if (posicion[1] == 0 or laberinto[posicion[0]][posicion[1] - 1] != " "):
                    print("Fin del laberinto!")
                else: move([posicion[0], posicion[1] - 1], posicion)
            else: move([posicion[0], posicion[1] + 1], posicion)
        else: move([posicion[0] + 1, posicion[1]], posicion)

    else:
        if (posicion[0] == 0 or laberinto[posicion[0] - 1][posicion[1]] != " "):
            if(posicion[1] == 9 or laberinto[posicion[0]][posicion[1] + 1] != " "):
                if (posicion[1] == 0 or laberinto[posicion[0]][posicion[1] - 1] != " "):
                    print("Fin del laberinto!")
                else: move([posicion[0], posicion[1] - 1], posicion)
            else: move([posicion[0], posicion[1] + 1], posicion)
        else: move([posicion[0] - 1, posicion[1]], posicion)

laberinto = [
    [" ", " ", " ", " ", " ", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", " ", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", " ", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", " ", "x", "x", " ", " ", " "],
    ["x", "x", "x", "x", " ", "x", "x", " ", "x", " "],
    ["x", "x", " ", " ", " ", "x", "x", " ", "x", " "],
    ["x", "x", " ", "x", "x", "x", "x", " ", "x", " "],
    ["x", "x", " ", " ", " ", " ", " ", " ", "x", " "],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", " "],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", " "]
]

#MAIN
Inicio([0,0])