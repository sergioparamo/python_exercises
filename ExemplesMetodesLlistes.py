# Nom: Sergio Paramo Escudero
# Date: 21/04/2020

# ******** OPERACIONES CON LISTAS *********


# .append(x) Agrega contenido al final de la lista
lista = [1, 2, 3, 4]
lista.append(5)
print("append " + str(lista))
print()

# .insert(x, y) Inserta en la lista el valor deseado (y) en la posición deseada (x)
listaInsert = ['Ronaldinho', 'Ronaldo', 'Casillas']
listaInsert.insert(0, 'Messi')
print("insert " + str(listaInsert))
print()


# .remove(x) Elimina un elemento de la lista que no conocemos su posición
listaRemove = listaInsert
listaRemove.remove('Ronaldinho')
print("remove " + str(listaRemove))
print()


# .sort() Ordena la lista de números
listaSort1 = [15, 6, 7, 3, 0, 4]
listaSort1.sort()
print("sort " + str(listaSort1))
print()

     # Tambien se puede usar con caracteres
listaSort2 = ['a', 'z', 'k', 'ñ', 'f']
listaSort2.sort()
print("sort " + str(listaSort2))
print()

      #Y ordenar la lista a la inversa

listaSort1.sort(reverse=True)  # Ordena la lista de mayor a menor
print("sort reverse " + str(listaSort1))
print()


# .sorted() Ordena la lista original pero no la modifica, obtiene una lista igual ordenada

listaSorted = [5, 3, 8, 2]
print("sorted " + str(sorted(listaSorted)))
print('sin el sorted ' + str(listaSorted))
print()


# .reverse() Vuelve la lista del revés
listaReverse = [1, 2, 3, 4, 5]
listaReverse.reverse()
print("reverse " + str(listaReverse))
print()

# .pop(x) Elimina el valor de la posición indicada. Si la función .pop() se encuentra vacía, eliminará el último valor
listaPop = [2, 4, 6, 78, 3, 5]
listaPop.pop(3+2)
print("pop " + str(listaPop))
print()

# .extend() Extiende la lista arreglandole varios elementos al final
listaExtend = [1, 2, 3, 4, 5]
listaExtend.extend([6, 7, 8])
print("extend " + str(listaExtend))
print()

# .index(x) Busca el valor deseado en la lista y devuelve su posición
listaIndex = ['Arroz', 'Lentejas', 'Pescado', 'Carne', 'Cereales', 'Champú']
print("index: " + str(listaIndex.index('Cereales')))
print()

# .count(x) Cuenta las veces que hay X valor en la lista
listaCount = [1, 2, 3, 4, 1, 1, 1, 5, 2, 3, 8, 4, 1, 2, 5, 3, 3, 4]
listaCount2 = ['Pablo', 'Iñigo', 'Alex', 'Carlos', 'Pablo']
print("count numeros: " + str(listaCount.count(1)))
print("count nombres: " + str(listaCount2.count('Pablo')))







