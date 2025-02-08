# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/Python Básico/Clase6")

# %% Definicion de funciones
     # Dos principios:
         # Reusabilidad
         # Modularidad

# Sintaxis
def funcion1():
    print("==================")
    print("Ejecucion de la funcion 1")
    print("==================")
    print("\n")
    
# %% Veamos un uso de la funcion : funcion1

for vez in range(5):
    funcion1()
    
# %% funcion1 devuelve nada

variable1 = funcion1()

type(variable1)

# %% Definicion de una funcion con un unico argumento y que devuelve
# un unico valor/output 

def funcion2(x):
    import random as rnd
    t = rnd.randint(x,x+666)
    return t**2

# %% Veamos una limitacion de funcion2

otp1 = funcion2(3.14159)

otp2 = funcion2(13)

type(otp2)

# %% funcion que recibe mas de un valor y devuelve mas de un valor

def funcion3(x1,x2,x3):
    y1 = x1+x2
    y2 = x2**(0.13*x3)
    y3 = 12.8/x1
    return (y1,y2,y3)

# %% Uso de funcion3

t1 = funcion3(12,-10,0.02)
t1

# Modificar el output t1 de funcion3
t1_oper = list(t1)
t1_oper[1] = 0

# %% Carguemos en memoria un conjunto de datos

# modificacion del directorio de trabajo
import os
# Si quiero ver los archivos de mi directorio en el que me 
# trabajando debo escribir os.listdir()
os.chdir("C:/Users/RODRIGO/Desktop/Python Básico/Clase6")

# Carguemos el dataset en memoria : modulo csv

# Modulo csv sirve para manipular dataset
import csv
# la 2da componente "r" indica que tiene permiso de lectura
with open("babyNamesUSYOB-mostpopular.csv","r") as file:
    lecturaCSV = csv.reader(file)

# Tipo de dato
type(lecturaCSV)

# Ejecutemos la variable lecturaCSV
lecturaCSV

# Mostremos fila a fila cada elemento de lecturaCSV
# para esto debo tener abierto el archivo y ejecutar
# las siguientes 4 lineas de golpe
with open("babyNamesUSYOB-mostpopular.csv","r") as file:
    lecturaCSV = csv.reader(file)
    for fila in lecturaCSV:
        print(fila)
# cada manipulacion que haga con mi data set siempre antes
# debo tener abierto el dataset con with open
# vamos a guardar todo nuestro dataset en una lista en blanco

# %% Empaquetemos en una lista cada fila de lecturaCSV

# Creamos una lista de nombres en blanco
ListaNombre = []

with open("babyNamesUSYOB-mostpopular.csv","r") as file:
    lecturaCSV = csv.reader(file)
    for fila in lecturaCSV:
        ListaNombre.append(fila)

# %% Guardemos cada columna del dataset en una lista

# Lista para el año
ListaYear = list()
# Lista para el nombre
ListaNombres = []
# Lista para el sexo
ListaSex = list()
# Lista de frecuencias
ListaFreq= []

with open("babyNamesUSYOB-mostpopular.csv","r") as file:
    lecturaCSV = csv.reader(file)
    for fila in lecturaCSV:
        ListaYear.append(fila[0])
        ListaNombres.append(fila[1])
        ListaSex.append(fila[2])
        ListaFreq.append(fila[3])

# Eliminemos la primera componente de cada lista recientemente creada
# [1:] significa desde el segundo elemento hasta el final
ListaYear = ListaYear[1:]
ListaNombres = ListaNombres[1:]
ListaSex = ListaSex[1:]
ListaFreq = ListaFreq[1:]        

# %% Implementar una funcion que reciba el nombre del archivo
# y devuelve cada columna en una lista

# %% Implemente una funcion que reciba una lista de nombres (primer argumento)
# y una letra (segundo argumento) y devuelva el numero de nombres que inician
# con esa letra

def CuentaNombres(lista,letra):
    
    """
    Funcion que cuenta el numero de nombres que pertenecen al argumento
    lista e inician con el argumento letra
    
    Parameters
    ----------
    lista : list
         Lista de nombres
    
    letra : str
         Letra a considerar
    
    Returns
    -------
    NumLetra : int
    
    """
    
    
    # Contador
    NumLetra = 0
    # Usamos una estructura repetitiva (y el hecho de que una lista es un
    # objeto iterable) para barrer todos los elementos de la lista
    # y contar aquellos que inician con letra
    for nombres in lista:
        if nombres[0] == letra:
            NumLetra = NumLetra + 1
    return NumLetra

# %% probemos CuentaNombres
CuentaNombres(ListaNombres[:100001],"P")

CuentaNombres(ListaNombres,"P")

# %% Argumentos por posicion

# Por la definicion de la funcion CuentaNombres, esta recibe como primer
# argumento un objeto de tipo list y como segundo argumento un caracter

ListaTemp = ListaNombres[666:6667]
LetraInicial = "H"
CuentaNombres(ListaTemp, LetraInicial)

# %% Argumentos por nombres

CuentaNombres(letra = "W", lista = ListaTemp)


# %% Funciones con valores por defecto

# ley de Coulomb

def coulomb(q1,q2,d,k=9*10**9):
    return(k*q1*q2)/(d**2)

# %% argumentos por posicion
coulomb(5.6*10**(-9),3.1*10**(-11),0.01,9.01*10**9)

# %% argumentos por nombre

coulomb(d=0.0002, k = 9.015*10**9, q1= 25*10**(-6), q2 = 0.13*10**(-6))

# %% Funciones con argumentos de longitud variable

# consideremos la funcion
def adicion1(x1,x2):
    return x1+x2

# Llamada de la funcion adicion1 por posicion
adicion1(12,9.6)

# Llamada de la funcion adicion1 por nombre
adicion1(x2=-12.5,x1=15.9)

# Una primera forma de considerar una funcion con un numero
# de argumentos variables es empaquetando estos argumentos 
# en una lista

def adicion2(numeros):
    """
    Sumar todos los elementos de la lista numeros

    """
    sumaTotal = 0
    for elemento in numeros:
        sumaTotal = sumaTotal + elemento
    return sumaTotal

# Llamadas a las funcion adicion2
adicion2([-12.5,15.9])
adicion2([-12.5,15.9,-12.3,36.9,9.6])

# %% Numero de argumentos variable

  # Si tiene dos argumentos, la funcion debe retornar el
  # producto de los argumentos
  
  # Si tiene tres argumentos, la funcion debe retornar el promedio
  # aritmetico de las entradas
  
def Operaciones1(*argumentos):
    if len(argumentos) == 2:
        return argumentos[0]*argumentos[1]
    elif len(argumentos) ==3:
        return sum(argumentos)/len(argumentos)
    else:
        return "Numero de argumentos invalido"


# %% llamadas a la funcion Operaciones1

Operaciones1()
Operaciones1(10,12)
Operaciones1(15,8,2)

# Notemos que es muy simple el uso de funciones con un numero
# variable de argumentos usando la estrategia de Operaciones1
# sin embargo no puedo hacer llamadas a la funcion por nombres

# %% Uso de kwargs: para solucionar el problema anterior

def adicion3(**kwargs):
    # Usar una variable de almacen para suma
    sumaTotal = 0
    for llave_kwargs, valor_kwargs in kwargs.items():
        print(llave_kwargs,valor_kwargs)
        sumaTotal = sumaTotal + valor_kwargs
    return sumaTotal

# %% llamemos a la funcion adicion3 con los argumentos
# por nombres

adicion3(p1=12,p2=13,p3=45)


# Obs :  Esto implica que podemos pasar a esta funcion (adicion3)
# un dato de tipo diccionario
datos = {"g1":9.81, "euler":2.71, "pi":19.8}
adicion3(**datos)

# %% Obliguemos a que la funcion trabaje con los argumentos c1, l1

def Operaciones2(**kwargs):
   #kwargs funciona como un diccionario
   if(("c1" in list(kwargs.keys())) & ("l1" in list(kwargs.keys()))):
       #kwargs.keys() me da todas las llaves de kwargs
       #list(kwargs.keys()) me genera una lista de dichas llaves
       print("Ejecucion permitida. Arrancando Jarvice !!!")
   else:
       print("Usuario : Lee la documentacion")
 
# para que corra mi codigo, mis argumentos deben aparecer explicitamente
# es decir aparecen c1,l1 con sus respectivos valores


# %%

Operaciones2(g1=12.5,pi=4,e=56)
Operaciones2(c1="Hola",l2="Mundo")
Operaciones2(c1=12.8, l1=15.9)

# %% Manejo de Errores y excepciones
# Errores que se generan al correr el codigo, este manejo
# evitara que todo nuestro trabajo se arruine por un error

# Definamos un conjunto de variables
c=12.9
d=-34.2

# Realicemos operaciones
h= c+d
h

# %%

# Operando llegamos a:

p=c*d/0
p

# %%

f = d*p
f

# %% 

# Otra excepcion
"12" + 9.8

# %% Lista de excepciones integradas en python


locals() # me muestra todo lo que hay en memoria ahorita
# locals()["__builtins__"] es un onjeto
# Las excepciones son parte de los metodos que
# yo puedo aplicar a los objetos


dir(locals()["__builtins__"])

# ['ArithmeticError',
#  'AssertionError',
#  'AttributeError',
#  'BaseException',
#  'BlockingIOError',
#  'BrokenPipeError',
#  'BufferError',
#  'BytesWarning',
#  'ChildProcessError',
#  'ConnectionAbortedError',
#  'ConnectionError',
#  'ConnectionRefusedError',
#  'ConnectionResetError',
#  'DeprecationWarning',
#  'EOFError',
#  'Ellipsis',
#  'EnvironmentError',
#  'Exception',
#  'False',
#  'FileExistsError',
#  'FileNotFoundError',
#  'FloatingPointError',
#  'FutureWarning',
#  'GeneratorExit',
#  'IOError',
#  'ImportError',
#  'ImportWarning',
#  'IndentationError',
#  'IndexError',
#  'InterruptedError',
#  'IsADirectoryError',
#  'KeyError',
#  'KeyboardInterrupt',
#  'LookupError',
#  'MemoryError',
#  'ModuleNotFoundError',
#  'NameError',
#  'None',
#  'NotADirectoryError',
#  'NotImplemented',
#  'NotImplementedError',
#  'OSError',
#  'OverflowError',
#  'PendingDeprecationWarning',
#  'PermissionError',
#  'ProcessLookupError',
#  'RecursionError',
#  'ReferenceError',
#  'ResourceWarning',
#  'RuntimeError',
#  'RuntimeWarning',
#  'StopAsyncIteration',
#  'StopIteration',
#  'SyntaxError',
#  'SyntaxWarning',
#  'SystemError',
#  'SystemExit',
#  'TabError',
#  'TimeoutError',
#  'True',
#  'TypeError',
#  'UnboundLocalError',
#  'UnicodeDecodeError',
#  'UnicodeEncodeError',
#  'UnicodeError',
#  'UnicodeTranslateError',
#  'UnicodeWarning',
#  'UserWarning',
#  'ValueError',
#  'Warning',
#  'WindowsError',
#  'ZeroDivisionError',

# Definamos una lista de excepciones

Excepciones = ['ArithmeticError',
 'AssertionError',
 'AttributeError',
 'BaseException',
 'BlockingIOError',
 'BrokenPipeError',
 'BufferError',
 'BytesWarning',
 'ChildProcessError',
 'ConnectionAbortedError',
 'ConnectionError',
 'ConnectionRefusedError',
 'ConnectionResetError',
 'DeprecationWarning',
 'EOFError',
 'Ellipsis',
 'EnvironmentError',
 'Exception',
 'False',
 'FileExistsError',
 'FileNotFoundError',
 'FloatingPointError',
 'FutureWarning',
 'GeneratorExit',
 'IOError',
 'ImportError',
 'ImportWarning',
 'IndentationError',
 'IndexError',
 'InterruptedError',
 'IsADirectoryError',
 'KeyError',
 'KeyboardInterrupt',
 'LookupError',
 'MemoryError',
 'ModuleNotFoundError',
 'NameError',
 'None',
 'NotADirectoryError',
 'NotImplemented',
 'NotImplementedError',
 'OSError',
 'OverflowError',
 'PendingDeprecationWarning',
 'PermissionError',
 'ProcessLookupError',
 'RecursionError',
 'ReferenceError',
 'ResourceWarning',
 'RuntimeError',
 'RuntimeWarning',
 'StopAsyncIteration',
 'StopIteration',
 'SyntaxError',
 'SyntaxWarning',
 'SystemError',
 'SystemExit',
 'TabError',
 'TimeoutError',
 'True',
 'TypeError',
 'UnboundLocalError',
 'UnicodeDecodeError',
 'UnicodeEncodeError',
 'UnicodeError',
 'UnicodeTranslateError',
 'UnicodeWarning',
 'UserWarning',
 'ValueError',
 'Warning',
 'WindowsError',
 'ZeroDivisionError']
               
#
# Numero de excepciones

len(Excepciones)

# En total python provee 72 excepciones para windows

# %% Veamos la excepcion FloatingPointError

# Veamos la documentacion de la excepcion FloatingPointError
help(FloatingPointError)

# Documentacion de ZeroDivisionError
help(ZeroDivisionError)

# %% Calculemos el reciprocro de cada elemento en una lista
# conformada por algunos numeros

# Lista de datos

ListaDatos = [12,17,-11,0,1,5,3]

# Calculemos el inverso de cada elemento

for elemento in ListaDatos:
    print(1/elemento)

# %% Resolvamos ese inconveniente

# Administrar/manejar las excepciones
# sentencias try y except

import sys
for elemento in ListaDatos:
    try: #sirve cuando todo va bien
        print("Input", elemento)
        print("El reciprocro", 1/elemento)
    except:
        print("==========================")
        print("Esta operacion es ilegal")
        print("Excepcion", sys.exc_info()) #para mostrar cual es el error sys.exc_infor()
        print("Continua hasta terminar con todos los datos !!!")
        print("==========================")


# %% Mejoremos el manejo de excepciones (de manera especifica)
try:
    print("Aca colocamos el codigo en caso todo esta correcto")
except ValueError:
    print("Obtuviste una excepcion: ValueError")
except (ZeroDivisionError, TypeError):
    print("Implementa un conjunto de operaciones mas adecuado")
except:
    print("No imagine otra excepcion. Entonces guardamos todo lo procesado")
























































































































