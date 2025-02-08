# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/Python Básico/Clase4")

# %% Definicion de tuplas
# Se usaran parentesis
# los elementos se separan por comas
# Las tuplas son objetos inmutables
# Los elementos de una tupla tambien pueden ser de diferente naturaleza



# Primera tupla
t1 = ()

# Definamos mas tuplas
t2 = ("frutas","arroz","cebolla",3.25,5.65,2)
t3 = (True, 3**(2.8), ["uno", "dos", "III"], ("Cuarta", "Clase"))

# Acceso a los elementos de una tupla
# Usamos indices enteros : 0,1,2 (positivos)
# Si leemos de derecha (final) a izquierda (inicio) los indices son negativos

# Segundo elemento de t3
t3[1]

# Penultimo elemento de t3
t3[-2]

# %% Metodos de interes que podemos aplicar a una tupla
dir(tuple)
# 'count',
# 'index'

# Para aprender a manipular/trabajar/usar un metodo determinado
# usamos help

# El metodo count
help(t1.count)

# Un ejemplito
t4 = (1,21,2|1,12,12,12,1,21,1,1,1,12,2,2,21,4)

#
# Cuantas ocurrencias tiene el numero 1
t4.count(1)

# Cuantas veces aparece el numero m.pi en t4

import math as m
t4.count(m.pi)

# Definamos otra tupla
t5 = ([],2,3,4,123,1231,[],[],[],"cadena","as","math")
t5.count([])

# El metodo index
t4.index(1)

# %% Diccionario

# Definicion de un diccionario
d1 = {}
type(d1)

# En un diccionario cada elemento es un par llave:valor
d2 = {"uno":1,"dos":"II", "tres":3}

# Acceso a sus elementos : por intermedio de las llaves
d2["uno"]
d2["tres"]
d2["Hola"]

# Metodos de un diccionario
dir(dict)

# 'clear',
# 'copy',
# 'fromkeys',
# 'get',
# 'items',
# 'keys',
# 'pop',
# 'popitem',
# 'setdefault',
# 'update',
# 'values'


# Definamos mas diccionarios
d3 = {"one":[True, False], "two":("Sexo","Edad"), 3:{0:1,1:2,2:3}}
d3["one"]
d3[3][0]

# Agreguemos un elemento mas a un diccionario ya definido
d3["cuatro"] = "four"

d4 = {"one":[True, False], "two":("Sexo","Edad"),3:{0:1,1:2,2:3}}

# %% El metodo clear

# Documentacion
help(d1.clear)

# Apliquemos el metodo clear al objeto d4
d4.clear()

# %% El metodo copy

# Documentacion
help(dict.copy)

d5 = d3
d5["one"] = 111

# Lo adecuado para crear una copia de un diccionario (independiente del original)
# diccionario original se usa el metodo copy

# Creamos d6 como copia de d3
d6 = d3.copy()
d6[4] = (4,4,4,4)

# %% El metodo fromkeys

# Documentacion
help(d6.fromkeys)

d7 = {}
d7.fromkeys("123")

d8 = {}
d8.fromkeys(["Comas","San Martin","Rimac","Chorrillos"])

d9 = {}
d9.fromkeys(("Piura","Lambayeque","Pacasmayo","Paita"),"Vacio")

# Luego yo puedo modificar cada uno de esos valores
d9["Piura"] = 123
d9["Lambayeque"] = 95
d9["Paita"] = 26

# %% El metodo get

# Documentacion
help(d8.get)

# Obtengamos el valor asociado a la llave "Piura" del diccionario d9
d9["Piura"]

# Que ocurre si utilizando la sintaxis anterior, la llave no existe
d9["Pacasmayo"]

# Usemos el metodo get
d9.get("Pacasmayo")

# Apliquemos get a d3

d3.get(4,"La llave no existe")

# %% El metodo items

# Documentacion
help(dict.items)

# apliquemos items al objeto de tipo diccionario d2
d2_items = d2.items()
type(d2_items)
dir(d2_items)

# Leamos la documentacion del unico metodo de interes de un objeto de
# tipo dict_items
help(d2_items.isdisjoint)

# %% El metodo keys

# Documentacion
help(dict.keys)
d3.keys()
d3.keys()[0]

# %% Aprovechemos un poco nuestra experiencia

# transformamos a una lista el d2_items
list(d2_items)

# y luego accedemos a sus elementos
list(d2_items)[0]
list(d2_items)[-1]

list(d3.keys())[0]

# %% El metodo pop sirve para eliminar elementos llave:valor

# Documentacion
help(d3.pop)

d3.pop("one")

d3.pop("Hola")

# %% El metodo popitem devuelve el ultimo elemento ya que lo elimina

# Documentacion
help(d1.popitem)

# Apliquemos popitem a d2
d2.popitem()

# %% Apliquemos popitem a d3
d3.popitem()

# %% El metodo setdefault

# Documentacion
help(d1.setdefault)

d1.setdefault("Clase","Cuarta")
d1.setdefault(666,"HOLA MUNDO")
d1.setdefault("Clase")

# %% El metodo update

# Documentacion
help(d3.update)

d1

# Documentacion
help(d3.update)

d1.update({"uno":"1" , "dos":"2"})

# %% El metodo values

# Documentacion
help(d1.values)

d1.values()
list(d1.values())

# %% IF

# Sintaxis basica de una estructura if

# ===========================================
# if expresion:
#     conjunto
#     de sentencias
# ===========================================

# Definamos una variable entera
num=14
if num >= 0:
    print("La variable ", num, "es mayor o igual a cero")

num = float(input("Ingrese un numero punto flotante"))
if num>=0:
    print("La variable ", num, "es mayor o igual a cero")
    
# %% IF-ELSE


# Sintaxis
# ====================================================
# if expresion:
#    sentencia 1
#    sentencia 2
# else:
#    sentencia 3
#    sentencia 4
# ====================================================

# Pidamos al usuario que ingrese un numero entero
num_entero = int(input("Ingresa una variable entera "))
if num_entero>=0:
    print("El valor ingresado es mayor o igual a cero")
else:
    print("El valor ingresado es menor a cero")
    
# %% Numero par

NumP = int(input("Ingresa un numero entero"))
if NumP%2 == 0:
    print(NumP , "es par")
else:
    print("El valor ingresado ", NumP , "No es par")

# %% Estructura de decision anidado
#====================================
# if exp1:
#     sentencia1
#     sentencia2
#     if exp2:
#         sent1
#         sent2
#     else:
#         sent3
#         sent4
#         sent5
# else:
#     sentencia3
#     sentencia4
#     sentencia5
#===================================    
    
 # Analicemos la paridad de un numero entero   
 
Num1 = int(input("Ingresa un numero entero "))
if Num1>0:
    if Num1 % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")
else:
    print("El numero debe ser > 0")

# %% IF-ELIF-ELSE

#======================================
# if cond1: 
#     sentencia1
#     sentencia2
#     sentencia3
# elif cond2:
#     sentencia4
#     sentencia5
#     sentencia6
#     sentencia7
# elif cond3:
#     sentencia8
# else:
#     sentencia9
#     sentencia10
#     sentencia11
#======================================   
    
# Pidamos al usuario una vocal : a e i o u

Vocal =input("Ingresa una vocal")
# actualizamos vocal a minuscula
Vocal = Vocal.lower()
if len(Vocal)>1:
   print("Una vocal es una cadena de caracteres con un unico elemento")
else:
   if Vocal == "a":
        print("Ingresaste la primera vocal")
   elif Vocal == "e":
        print("Ingresaste la segunda vocal ")
   elif Vocal == "i":
        print("Ingresaste la tercera vocal")
   elif Vocal == "o":
        print("Ingresaste la cuarta vocal")
   elif Vocal == "u":
        print("Ingresaste la ultima vocal")
   else:
        print("No ingresaste vocal alguna")
    
# %% Estructura de repeticion for

# Objeto range
help(range)

# ejemplos de range
range(8)   
range(12,19)
range(1,99,3) 

# Usemos el constructor list
list(range(8))   
list(range(12,19))
list(range(1,99,3))

# Variables iterables:
    # cadenas de caracteres
    # listas
    # tuplas
    
# %% primer ejemplo de uso de la estructura FOR

#for elemento in conjunto(iterable)


# para todo elemento que esta en el range(5)
for elemento in range(5):
    print(elemento**2)
    
# %% Segundo ejemplo de for

for e in "holaMUndo":
    print(e + "2024")

# %% Tercer ejemplo de FOR

# Definamos una lista
ListaX = [True,23,"PIT2024",3.18**(1/2.71),()]

# Deseo obtener el tipo de dato de cada elemento
# de la variable ListaX

for X in ListaX:
    print(type(X))

# %% Cuarto ejemplo de for

tupla = (12,13,9,3,5,7)

# Elevemos cada elemento de la variable tupla
# al cuadrado

for t in tupla:
    print("Elemento ", t, "Cuadrado", t**2)

# %% quinto ejemplo

# Generemos una lista con valores aleatorios

# Carguemos el modulo random
import random as rnd

# Definamos el numero de elementos de nuestra lista

NumElements=int(input("Ingresa el numero de elementos a generar"))

# Iniciamos creando una lista en blanco
Data = []

for elemento in range(NumElements):
    Data.append(rnd.random())
    
print("La lista generada es: \n ", Data)


# %% Generemos una lista con numeros enteros

# El intervalo para estos numeros enteros debe ser dado 
# por el usuario

# Cargamos el modulo random
import random as rnd

# Definamos el numero de elementos a generar en nuestra lista
N = int(input("Ingresa el numero de elementos a generar "))


# limite inferior
Lim_inf = int(input("Ingresa el limite inferior "))

# Limite superior
Lim_sup = int(input("Ingresa el limite superior"))

# Mensaje informativo
print("""
      Intervalo : [%d,%d]
      
      """%(Lim_inf,Lim_sup))

if((N>0) & (Lim_inf < Lim_sup)):
    print("Generacion de una lista con elementos enteros")
    #
    # Creamos una lista en blanco para almacenar nuestros elementos
    # aleatorios generados
    DataGen = list()
    # Usamos una estructura repetitiva para generar los elementos
    # de la variable DataGen
    for i in range(N):
        # Generamos el entero aleatorio en [Lim_inf,Lim_sup]
        r=int(rnd.random()*(Lim_sup - Lim_inf) + Lim_inf)
        DataGen.append(r)
else:
    print("Valores ingresados INCORRECTOS !!!")
    

# %%
# Para DataGen
  # Calcule el numero de elementos mayores que 0
  # Calcule el numero de elementos que se encuentren en [-3.14,3.14]
  # Calcule el numero de elementos multiplos de 13
  # Calcule la media armonica de los elementos mayores a 150
  # Calcule el minimo valor de DataGen
  # Calcule la desviacion estandar de los elementos de DataGen
  # Cuantas veces se repite el numero 128
  # Cual es el elemento de DataGen que se repite un mayor numero de veces
  # Construye un diccionario con las siguientes caracteristicas:
      # Las llaves seran los elementos en formato str
      # sus valores correspondientes seran los elementos de DataGen
      #
      # Por ejemplo {"-43":-43 , "227":227 , .... } tiene 5000 elementos



















