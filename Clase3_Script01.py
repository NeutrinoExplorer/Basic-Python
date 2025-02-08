# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/Python Básico/Clase3")



# %% Lista de funciones que componen al modulo os
dir(os)

# Documentacion de chdir

help(os.chdir)

# Documentacion de la funcion listdir

help(os.listdir)

# Documentacion de la funcion getcwd

help(os.getcwd)

os.getcwd()
os.listdir()


# %% Definicion de variables

x1 = 12
x2 = "Tercera Clase"
x3 = True
x4 = 0.5**(1.3)

# %% Documentacion del modulo math

import math as m
help(m)



# %% Listas

#Las listas son objetos iterables
# Definicion : Usando corchetes
#los elementos de la lista pueden ser heterogeneos
Lista1 = [12,13,9,4,True,"XII",3.14,[1]]
Lista2 = []

# Tipo de dato
type(Lista1)
type(Lista2)

# Python es dinamicamente tipado
Lista1 = 0.0

# Luego la variable Lista1 puede volver a ser
# una lista

import math as m
import random as rnd
Lista1 = [m.pi**2, m.sin(m.radians(45)), rnd.gauss(3.14,9)]

# %% Propiedades de una lista

# Una lista es un objeto iterable: Yo puedo acceder a sus 
# elementos mediante el uso de indices
Lista1[0]

# Ultimo elemento
Lista1[-1]

# Los indices de izquierda a derecha : 0,1,2,3,....
# Los indices de derecha a izquierda : -1,-2,-3, ....

#
Lista3 = ["a","b","c"] + [12,13,14]
type(Lista3)

#
Lista4 = ["uno"] * 3

#
Lista5 = Lista4*2

# Penultimo elemento de Lista5
Lista5[-2]

# Una lista es editable
Lista3
# Modificar el ultimo elemento
Lista4[-1] = m.exp(0.01)

# Seleccion de un subconjunto de elementos de una lista
# seleccionemos los 3 primeros elementos de Lista5
Lista5[:3] #va de Lista5[0] -> Lista5[3-1]

# %% Una lista tambien es un objeto de python
#como es objeto entonces tiene asociada una lista de metodos

# Lista de metodos que se pueden aplicar a una lista
dir(Lista1)
#tambien se puede obtener los metodos como
dir(list)
# 'append',
# 'clear',
# 'copy',
# 'count',
# 'extend',
# 'index',
# 'insert',
# 'pop',
# 'remove',
# 'reverse',
# 'sort'

#Diferencia de un metodo de una funcion
# Una funcion es algo solitaria
# Un metodo esta asociado siempre a un objeto

# %% El metodo append

# No sabemos como usar append?
help(Lista1.append)

# Definamos una lista en blanco
l1 = []
print("l1 = " , l1)

# Apliquemos el metodo append a l1
l1.append("NuevoElemento")
print("El nuevo valor de l1 es : " , l1)

# Otro ejemplito
Lista5.append([2,3,4])
print("El nuevo valor de Lista5 es : " , Lista5)

# Agreguemos nuevamente elementos a la variable Lista5
Lista5.append([m.cos(m.pi), m.exp(2.9)])

# Observacion
# Ultimo elemento de Lista5
Lista5[-1]
Lista5[-1][0]
Lista5[-1][1]

# Usemos una lista para definir un vector en R4
Vec1_R4 = [1,2,3,4]

# Usemos una lista para definir una matriz
Mat1 = [[12,4,5],[9,4,6],[m.pi,m.exp(1),2]]
Mat1[1][2] 
Mat1[0][2]

# %% El metodo clear

# Documentacion
help(Mat1.clear)

l1.clear()

# Apliquemos clear a Mat1
Mat1
Mat1.clear()
Mat1

# Recordar que para eliminar una variable: del
# Eliminemos las variables l1, Lista2 y Mat1
del l1
del Lista2
del Mat1

# %% El metodo copy

# El metodo usual para crear una copia de una
# variable

Vec2 = Vec1_R4

# Modifiquemos el primer elemento de la copia Vec2
Vec2[0] = "Cero"

# La manera adecuada de crear copias de listas
# es usando el metodo copy

# Documentacion del metodo copy

# Veamos un ejemplito
Vec1_Copy = Vec1_R4.copy()

# Modifiquemos el primer elemento de Vec1_Copy
Vec1_Copy[0] = 0

# %% El metodo count

# Documentacion
help(list.count)

# Creemos una lista
Lista6 = [1,2,3,21,1,1,21,2,12,45,45,4,0]

# Apliquemos count para contar el numero de veces
# que aparece el numero 1
Lista6.count(1)

# Numero de veces que aparece el numero 12
Lista6.count(12)

# Numero de veces que aparece el numero 100
Lista6.count(100)

# %% El metodo extend

# Documentacion
help(Lista1.extend)

#
Lista6.extend("HolaMundo")
Lista5.append([12,12,12])
Lista5.extend([12,12,12])

# %% El metodo index

# Documentacion
help(list.index)

Lista5

# Apliquemos index a Lista5 con argumento 12
Lista5.index(12)

Lista5.index ("Python")


# %% El metodo insert

# Documentacion
help(Lista5.insert)


Lista5.insert(6,True)
Lista5

# %% El meetodo pop

# Documentacion
help(list.pop)

Lista6

Lista6.pop()

Lista6.pop(13)

# %% El metodo remove

# Documentacion
help(list.remove)

Lista6.remove(21)

# %% El metodo reverse

# Documentacion
help(Lista6.reverse)

Lista6.reverse()

# %% El metodo sort

# Documentacion
help(Lista6.sort)

Lista1.sort()









