# ...............................................................................................
# ABS: devuelve el valor absoluto de un numero
# si x es un numero complejo devolvera la raiz cuadrada de la suma de los cuadrados
# de la parte real y la parte imaginaria

print('***** FUNCION  ABS ********')
print('   ')
float = -52.26
print('Abs de un float: ', abs(float))

int = 5
print('Abs de un numero int: ', abs(int))

complex = (3 - 4j)
print('Abs de un numero complejo: ', abs(complex))
print('   ')
print('   ')

# ...............................................................................................
# all(iterable)
# devuelve true si hay numeros en los elementos del iterable (que no sean 0), o si no esta vacio

print('***** FUNCION  ALL ********')
print('   ')
print('Esta vacio: ', all([]))
print('Contiene numeros: ', all([6, 7]))
print('Contiene un "none": ', all([6, 7, None]))
print('Contiene un zero: ', all([0, 6, 7]))
print('Contiene numeros: ', all([9, 8, [1, 2]]))
print('Contiene un [] vacio: ', all([9, 8, []]))
print('Contiene numeros y un [] en medio', all([9, 8, [1, 2, []]]))
print('Contiene un {}: ', all([9, 8, {}]))
print('Contiene numeros y palabras: ', all([9, 8, {'engine': 'Gcloud'}]))
print('   ')
print('   ')

# ...............................................................................................
# any(iterable)
# devuelve true si todos los elementos del iterable tiene valor true.
# si el iterable esta vacio devuelve false

print('***** FUNCION  ANY ********')
print('   ')
lis1 = [10, 20, 30, 40]
print(lis1)
print('todos los valores son true', any(lis1))
print('   ')

lis2 = [0, False]
print(lis2)
print('Todos los valores son falsos', any(lis2))
print('   ')

lis3 = [0, 10, 5, 15]
print(lis3)
print('Un valor es falso los otros ciertos', any(lis3))
print('   ')

lis4 = [10, 0, False]
print(lis4)
print('Un valor es cierto el resto falso', any(lis4))
print('   ')

lis5 = []
print(lis5)
print('El iterable esta vacio', any(lis5))
print('   ')
print('   ')


# ...............................................................................................
# apply(f,arg=(),keywords={})
# devuelve true si todos los elementos del iterable tiene valor true.
# si el iterable esta vacio devuelve false

def f(arg):
    print("Hola", arg, "!")


print('***** FUNCION  APPLY ********')
print('   ')

# ...............................................................................................
# bin(x)
# devuelve una cadena que se corresponde con la representacion binario del entero x

print('***** FUNCION  BIN ********')
print('   ')
print('Entero de 8: ', bin(8))
print('   ')

# ...............................................................................................
# bool(x)
# devuelve 0 si es falso, en caso contrario devuelve 1

print('***** FUNCION  BOOL ********')
print('   ')
print('8 es igual a 2?: ', bool(8 == 2))
print('8 es igual a 8?: ', bool(8 == 8))
print('   ')

# ...............................................................................................
# chr(x)
# devuelve una cadena de longitud 1 que representa el caracter correspondiente al codigo ASCII x

print('***** FUNCION  CHR ********')
print('   ')
print('Operador suma: ', chr(43))
print('Arroba: ', chr(64))
print('   ')

# ...............................................................................................
# divmod(x, y) Recibe 2 números y retorna el cuociente y el resto de la división
print('***** FUNCION  DIVMOD ********')
print('   ')
print("divmod(x, y) " + str(divmod(10, 2)))
print(" ")

# ...............................................................................................
# enumerate() Enumera el contenido de una lista
print('***** FUNCION  ENUMERATE ********')
print('   ')
mi_lista = ["costillas", "chuletas", "entrecot", "pechuga"]
print("enumerate() ")
for x, element in enumerate(mi_lista):
    print(x, element)
print(" ")

# ...............................................................................................
# eval() Evalua la expresión pasada por parámetro, un string
print('***** FUNCION  EVAL ********')
print('   ')
x = 23
y = 6
print("eval() ")
print(eval('x+y'))
print(" ")

# ...............................................................................................
# exec() Ejecuta  el contenido de la función que le pasamos como argumento en formato cadena
print('***** FUNCION  EXEC ********')
print('   ')
print("exec() ")
exec("lista = [1, 2, 3, 4, 5]")
exec("for item in lista: print(item, 'es un número entero')")
print(" ")


# ...............................................................................................
# filter(funcion, iterable) A partir de una lista o iterador y una función devuelve los elementos que cumplen la
# condición. En este ejemplo tenemos una función que revisa la lista y retorna true si el número es múltiples de 5

def multiple(numero):
    if numero % 5 == 0:
        return True


print('***** FUNCION  FILTER ********')
print('   ')
print("filter(funcion, lista)")
numeros = [2, 5, 10, 23, 50, 33]
print(list(filter(multiple, numeros)))
print(" ")

# ...............................................................................................
# getattr(object, name) Permite obtener el valor de un atributo indicando su nombre como una cadena
print('***** FUNCION  GETATTR ********')
print('   ')


class Empleado:
    pass


a = Empleado()
a.nombre = 'Pepe'
print("getattr(object, name)")
print(a.nombre)
print(getattr(a, 'edad', 30))
print(" ")

# ...............................................................................................
# hasattr(object, name) Retorna true si el objeto tiene como atributo la propiedad name
print('***** FUNCION  HASATTR ********')
print('   ')


class A:
    def Atributo1(self):
        pass


print("hasattr(object, name)")
print(hasattr(A, "Atributo1"))
print(" ")

# ...............................................................................................
# max(iterable) Retorna el elemento máximo de una lista
print('***** FUNCION  MAX ********')
print('   ')
max_list = [5, 8, 9, 6, 13, 1, 12]
print("max(iterable)")
print(max(max_list))
print(" ")

# ...............................................................................................
# min(iterable) Retorna el elemento mínimo de una lista
print('***** FUNCION  MIN ********')
print('   ')
print("min(iterable)")
print(min(max_list))
print(" ")

# ...............................................................................................
# open(file) Abre el archivo y devuelve su contenido siempre que se acompañe de .read()
print('***** FUNCION  OPEN ********')
print('   ')
print("open(file)")
text_file = open('Text.txt')
print(text_file.read())
print(" ")

# ...............................................................................................
# pow(x, y) Retorna X elevado a potencia de Y
print('***** FUNCION  POW ********')
print('   ')
print("pow(x, y)")
print(pow(10, 2))
print(" ")

# ...............................................................................................
# reversed(lista) Retorna la lista en orden inverso, de derecha a izquierda
print('***** FUNCION  REVERSED ********')
print('   ')
lista_A = [9, 1, 2, 8, 4, 5]
print("reversed(lista)")
print(lista_A)
print(list(reversed(lista_A)))
print(" ")

# ...............................................................................................
# round(x) Redondea X al entero más próximo
print('***** FUNCION  ROUND ********')
print('   ')
print("round(x)")
print(round(1.8))
print(" ")

# ...............................................................................................
# setattr(object, atributo, valor) Asigna un nuevo valor a un atributo del objeto, sino existe lo crea
print('***** FUNCION  SETATTR ********')
print('   ')


class Coche:
    color = "Rojo"
    precio = 12000


print("setattr(object, atributo, valor)")
print(getattr(Coche, 'color'))
setattr(Coche, 'color', 'Negro')
print(getattr(Coche, 'color'))
print(" ")

# ...............................................................................................
# str(object) retorna una representación como cadena del objeto pasado como parámetro
print('***** FUNCION  STR ********')
print('   ')
num = 58
print("str(object) ")
print(type(str(num)))
print(str(num))
print(type(num))
print(" ")

# ...............................................................................................
# sum(iterable) Retorna la suma total de los elementos d ela lista
print('***** FUNCION  SUM ********')
print('   ')
print("sum(iterable)")
print(sum(max_list))
print(" ")

# ...............................................................................................
# type(object) Retorna el tipo del objeto
print('***** FUNCION  TYPE ********')
print('   ')
n = 10
print(type(n))
print(" ")

# ...............................................................................................
# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1) Retorna el tipo del objeto
print('***** FUNCION  TYPE ********')
print('   ')
code_str = 'x=5\ny=10\nprint("sum =",x+y)'
code = compile(code_str, 'sum.py', 'exec')
print(type(code))
exec(code)
print(" ")

# ...............................................................................................
# delattr(object,name) Retorna el tipo del objeto
print('***** FUNCION  DELATTR ********')
print('   ')


class Coordenadas:
    x = 10
    y = -5
    z = 0


point1 = Coordenadas()

print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)

delattr(Coordenadas, 'z')

print('--Despues de borrar el objeto Z de la clase Coordenadas --')
print('x = ', point1.x)
print('y = ', point1.y)

# Da un error al querer printear un objeto de la clase eliminado
print('z = ', point1.z)
print("Nos devuelve un error ya que el objeto a printar no existe, ha sido eliminado por delattr")
print(" ")
