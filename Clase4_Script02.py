# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/Python Básico/Clase4")

# %% Estructura de repeticion : While

# siempre necesitaremos un contador
contador = 0
while contador<10:
    print("python" + "\tValor actual de contador" + str(contador)) 
    #\t significa un pequeño espacio en blanco
    #y actualizamos el valor de contador
    contador = contador + 1
    # la anterior linea es necesaria, pues
    # si no actualizamos la variable contador
    # la expresion booleana que evalua la estructura de repeticion while
    # nunca llegaria a ser falsa

# %% Considere el escenario don del valor de actualizacion es un aleatorio
import random as rnd

Numveces = 0
NumIter = 0
while Numveces < 20:
    NumIter = NumIter + 1
    print("Python" + "Numero de veces" + str(Numveces))
    # actualizamos Numveces con un aleatorio
    Numveces = Numveces + (rnd.randint(0,20))**(1/2)
    
print("Numero de iteraciones", NumIter)  
    
    
    
# %% Pidamos al usuario un numero diferente de cero
# si ingresa cero debe de pedir nuevamente el numero
# UPDATE al requerimiento : Solo se puede equivocar 3 veces consecutivas

# Pidamos una primera vez la variable numero
numero = int(input("Ingresa un numero diferente de cero"))

# Definamos un contador de veces
NumVezError= 0


while numero == 0:
   numero = int(input("Ingresa un numero diferente de cero"))
   # Actualizamos un contador de veces    
   NumVezError = NumVezError + 1
   if (NumVezError == 2) :
       # Esta asignacion logra que el while sea falso: concluyendo asi el while
       numero = 10
       print("Se te acabaron los intentos")

# %% Ingresar un conjunto no determinado de notas y calcular el promedio
# El valor 999. Indica el fin del ingreso de notas

nota = float(input("Ingrese una nota: "))

if nota != 999:
    # Variable acumuladora
    suma = nota
    # Variable contadora
    n = 1
    while nota != 999:
        nota = float(input("Ingrese una nota: "))
        if nota != 999:
          suma = suma + nota
          n = n+1    
        
    print("El promedio de notas ingresadas es: %.3f" %(suma/n))
else:
    print("No se ingresaron notas")

# %% La estructura match


    

















