# %% Primeros pasos
# Cargar modulos básicos y configurar el directorio de trabajo

import os
import math as m
import random as rnd

# Configurar mi directorio de trabajo
os.chdir("C:/Users/RODRIGO/Desktop/Python Básico/Clase5")

# %% Definicion de funciones

# Cada vez que yo use o modifique la definicion de la funcion
# debo ejecutar (cargar en memoria) el codigo fuente de mi funcion

def nombreFuncion(x,string,altura):
    print("Primera funcion en python")
    
    
    
# %% Ejecutar a mi primera funcion

# Este es un ejemplo de una funcion conn argumentos obligatorios
nombreFuncion("x",12,"1.98") 

# Otra ejecucion

nombreFuncion(3.14,True, ["UNICO"])

# Obs: En las funciones definidas por el usuario no se especifica
# el tipo de dato para cada argumento

# %% Mejoremos nuestra definicion de funciones

def ProdInter3D(v1,v2):
    """
    Funcion que calcula el producto interno de dos vectores en 3D
    
    Parameters
    ----------
    
    v1 : list
         Primer vector
    
    v2 : list
         Segundo vector
         
    Returns
    -------
    
    p_interno : float
    Representa el producto interno de dos vectores en R3
    

    """
    
    # Verifiquemos que los argumentos (v1,v2) son listas con 3 items

    if(len(v1)==3) & (len(v2)==3):
        p_interno = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    else : 
        print("El numero de elementos es inaceptable")
        
    # Output
    return p_interno

# %% Veamos un ejemplo de uso de ProdInter3d

import random as rnd

x1 = [rnd.random(),rnd.random()**2,1]
x2 = [0,0,1]

# Calculamos el producto interno de x1 con x2 usando ProdInter3D

ProdInter3D(x1,x2)    

# %% Ejemplito 

# Dado un texto contemos las vocales minusculas

def ContarVocales(texto):
    
    """
    
    Funcion que contara el numero de vocales (a,e,i,o,u) escritas en
    minusculas en el texto dado como argumento
    
    Parameters
    ----------
    texto : str
       Uno o mas parrafos de algun texto al cual se le contara 
       las vocales minusculas
    
    Returns
    -------
    vocales : dict
    vocales = {"a": Numero de veces que aparece a,
               "e": Numero de veces que aparece e,
               "i": Numero de veces que aparece i,
               "o": Numero de veces que aparece o,
               "u": Numero de veces que aparece u}
    
    """
    
    # Crear nuestro diccionario con las llaves adecuadas
    #para ver los metodos del diccionario
    dir(dict)
    vocales = {}.fromkeys("aeiou")
    
    # Inicializamos 5 variables para almacenar el numero de veces que aparece
    # cada vocal
    num_a = 0
    num_e = 0
    num_i = 0
    num_o = 0
    num_u = 0
    
    # Usaremos el hecho de que una cadena de caracteres es un objeto
    # iterables en python
    
    
    for caracter in texto:
        if caracter == "a":
            num_a = num_a + 1
        elif caracter == "e":
            num_e = num_e + 1
        elif caracter == "o":
            num_o = num_o + 1
        elif caracter == "u":
            num_u = num_u + 1
    # Rellenamos los valores de mi diccionario vocales
    vocales["a"] = num_a
    vocales["e"] = num_e
    vocales["i"] = num_i
    vocales["o"] = num_o
    vocales["u"] = num_u
    
    # Output
    return vocales

# %% Pruebas de ContarVocales

txt1 = "esta es la penultima clase del curso de python basico"

NumVocales = ContarVocales(txt1)
NumVocales
    

# %% Implementacion de la estrategia explicada en clase para el
# Metodo de la biseccion

def Met_Biseccion(a,b,f,N):
    """
    Metodo de la biseccion : Estrategia explicada en clase

    Parameters
    ----------
    a : float
        Limite izquierdo/inferior del primer intervalo de busqueda
    b : float
        Limite derecho/superior del primer intervalo de busqueda
    f : Regla de correspondencia de la funcion continua en [a,b]
        con la propiedad de que f(a)*f(b)<0
    N : int
        Numero de elementos de la sucesion a construir
        
    Returns
    -------
    c_aprox : Punto medio de cada intervalo de busqueda

    """
    # Trabajemos con copias de a y b
    a_n = a
    b_n = b
    
    # Implementacion de la estrategia ganadora
    
    for n in range(1,N+1):
        # Calculemos el punto medio
        # y la imagen de ese punto medio
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        # Actualizacion del intervalo de busqueda
        if f(a_n)*f_m_n <0:
            # Me quedo con el subinntervalo izquierdo
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n <0:
            # Me quedo con el subintervalo derecho
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Encontraste una solucion exacta")
            return m_n
        else:
            # Para los casos que no me los imagine
            print("El metodo de la biseccion falla")
            return None
    return (a_n + b_n)/2

# %% Ejemplito

def cuad1(x):
    return x**2 - x - 1
# Usemos nuestra implementacion del metodo de la biseccion para
# calcular aproximaciones a las raices

c1 = Met_Biseccion(-1,0,cuad1,20)
c2 = Met_Biseccion(1,2,cuad1,20)

# Mostremos los resultados
print("""
      
La funcion : f(x) = x**2 -x -1
continua en [-1,0] y en [1,2]
tiene como aproximaciones a sus raices :
    c1 = %f
    c2 = %f
    """%(c1,c2))
    
def J3_suma (j,m):
    a = (j(j+1)-m(m+1))**(1/2)
    b = (j,m+1)
    c = (a,b)
    return c
# %% Otro ejemplito 

def cubic1(x):
    return x**3 - x**2 + 2

r1= Met_Biseccion(-2, 0, cubic1, 5)
    
# %% Otro ejemplito mas
# Wolfram Al´pha:
    # representar graficamente exp(x)*(3.2*sin(x)-0.5*cos(x))
import math as m
def wolAlpha(x):
 return m.exp(x)*(3.2*m.sin(x)-0.5*m.cos(x))

# Apliquemos MetBiseccion
r1 = Met_Biseccion(2, 4, wolAlpha, 20)
r2 = Met_Biseccion(0, 1, wolAlpha, 10)

print("""
      raiz en [2,4] : %f
      raiz en [0,1] : %f
      
      """%(r1,r2))


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    