# Nom: Sergio Paramo Escudero
# Date: 20/04/2020

diccionario = {'Reptiles': 'Salamandra', 'Peces': 'Salmón', 'Mamiferos': 'Conejo', 'Arañas y alacranes': 'Tarantula'}
print("diccionario completo " + str(diccionario))
print()

# Printear un animal de una especie en particular
print("Animal mamifero: " + str(diccionario["Mamiferos"]))
print()

# len() Retorna el número de elementos que tiene el diccionario
print("len: "+str(len(diccionario)))
print()

# del() Elimina el valor introducido en la función
del (diccionario["Peces"])
print("La especie peces ha sido eliminada " + str(diccionario))
print()

# get(x) Retorna el valor que corresponde del diccionario. Si no existe devuelve None
print("get(x): " + str(diccionario.get("Salmón")))
print("get(x): " + str(diccionario.get("Reptiles")))
print()

# keys() Retorna una lista con las claves del diccionario
print("keys: " + str(diccionario.keys()))
print()

# values() Retorna una lista con los valores del diccionario
print("values: " + str(diccionario.values()))
print()

# items() Retorna una lista de los elementos del diccionario, tanto la clave como el valor
print("items: " + str(diccionario.items()))
print()

# popitem() Elimina el último valor del diccionario
print("popitem: " + str(diccionario.popitem()))
print()

# update(x) Actualiza el diccionario con los datos de otro diccionario
diccionario2 = {"Aves": "Gaviota", "Ranas y sapos": "Rana amarilla", "Insectos": "Escarabajo"}
diccionario.update(diccionario2)
print("diccionario actualizado " + str(diccionario))
print()

# Iterar con un for e imprimir los items del diccionario
print("Clave y valor con un for")
for items in diccionario.items():
    print(items)
print()

# Iterar con un for e imprimir solo la clave
print("Clave con for")
for clave in diccionario.keys():
    print("Clave = %s" % clave)
print()

# Iterar con un for e imprimir solo el valor
print("Valor con for")
for valor in diccionario.values():
    print("Valor = %s" % valor)
print()

# has_key() ('in') Se usa para saber si un elemento está dentro del diccionario, si está devuelve True, sino, False
print("has_key(): " + str('Cangrejos y camarones' in diccionario))
print("has_key(): " + str('Aves' in diccionario))
print()

# clear() Elimina los elmentos del diccionario
diccionario.clear()
print("clear: "+str(diccionario))
print()