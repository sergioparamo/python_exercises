# 1.- Funció que determina si dos llistes són iguals. Dos llistes són iguals si tenen igual longitud i els seus elements en cada índex també ho són.
from pip._vendor.distlib.compat import raw_input


def compararListas():
    print("****** FUNCION COMPARADOR DE LISTAS *******")
    print("Introduce dos listas y compararemos si son iguales")

    print("Introduce la longitud de las listas")
    longitud = lee_entero()

    lista1 = []
    lista2 = []

    print("Introduce los valores de la primera lista")

    i = 0
    while i < longitud:
        argumento = lee_entero()
        lista1.append(int(argumento))
        i += 1

    print("Lista nº 1 finalizada, introduce los valores de la segunda lista por favor")

    i = 0
    while i < longitud:
        argumento = input("Introduce un valor ")
        lista2.append(int(argumento))
        i += 1

    print("Recogida de valores finalizada, estas son las listas")
    print(lista1)
    print(lista2)

    print("¿Quieres compararlas o volver a empezar? (1/2)")
    opcion = lee_entero()
    while opcion != 1 or opcion != 2:

        if opcion == "1":
            print("Comparando listas...")
            i = 0
            contador = 0
            while i < 10:
                if lista1[i] == lista2[i]:
                    contador += 1
                    i += 1
                else:
                    i += 1
            if contador == 10:
                print("Las listas son iguales")
            else:
                print("Las listas no son iguales")
        elif opcion == "2":
            compararListas()
        else:
            print("Opcion no valida")



# 2.- Funció que rep una matriu d’enters i retorna una tupla amb la llista o vector de la suma de cada fila i un altre vector amb la suma de cada columna.

def sumaMatrix():
    print("****** FUNCION SUMA DE FILAS Y COLUMNAS DE MATRIZ *******")
    matrix = []

    for i in range(2):
        matrix.append([])
        for j in range(2):
            valor = int(input(("Introduce el valor de la fila " + str(i) + " columna " + str(j) + ": ")))
            matrix[i].append(valor)

    vectorFilas = []
    vectorColumnas = []

    for i in range(2):
        suma = sum(matrix[i])
        vectorFilas.append(suma)

    for i in range(2):
        sumaC = sum([fila[i] for fila in matrix])
        vectorColumnas.append(sumaC)

    for fila in matrix:
        print("[", end=" ")  # end= imprimr todos los valores de la lista
        for columna in fila:
            print("{:2}".format(columna), end=" ")  # {:2} es para dejar espacio entre valores de la matriz
        print("  ]")
        print("")

    print("Lista con la  suma de las filas")
    print(vectorFilas)
    print("")
    print("Lista con la  suma de las columnas")
    print(vectorColumnas)
    print("")

# 3.- Funció que determina si un número passat per paràmetre és primer.

def numeroPrimo(num):
    print("****** FUNCION SABER SI UN NUMERO ES PRIMO *******")
    for i in range(1, num):
        if num % i == 0:
            return True
    return False


# 4.- Funció que donat un número x retorna una llista infinita amb tots els múltiples de x.

def multiplesInfinitos():
    print("****** FUNCION LISTA INFINITA DE MULTIPLES *******")
    num = lee_entero()
    multiple = 1
    while True:
        print(num * multiple)
        multiple += 1

def menu():
    print("Selecciona una opción")
    print("1 - Comparar listas")
    print("2 - Mostrar la suma de las filas y las columnas de una matriz")
    print("3 - Comprobar si un número es primo")
    print("4 - Multiples infinitos de un número")
    print("5 - Finalizar programa")


# funcion para asegurarse de la lectura de un numero entero
def lee_entero():
    """ Solicita un valor entero y lo devuelve.
        Mientras el valor ingresado no sea entero, vuelve a solicitarlo. """
    while True:
        valor = raw_input("Ingrese un número entero: ")
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print("ATENCIÓN: Debe ingresar un número entero.")


opcionMenuPrincipal = 0
while opcionMenuPrincipal != 5:
    menu()
    opcionMenuPrincipal = lee_entero()
    if opcionMenuPrincipal == 1:
        compararListas()
    elif opcionMenuPrincipal == 2:
        sumaMatrix()
    elif opcionMenuPrincipal == 3:
        n = lee_entero()
        if numeroPrimo(n) is True:
            print("El numero " + str(n) + " es primo")
            print("")
        else:
            print("El numero " + str(n) + " no es primo")
            print("")
    elif opcionMenuPrincipal == 4:
        multiplesInfinitos()
    elif opcionMenuPrincipal == 5:
        print("Finalizando programa...")
    else:
        menu()
