import pandas as pd
import numpy as np

mi_lista = [1,2,3]
mi_lista.append(4)
print(".append() ", mi_lista)


#pop() elimina el elemento que le pongo entre () 

mi_lista = [1,2,3,4,5,6]
mi_lista.pop #si no le digo entre () el elemento, por defecto me elimina el último elemento
print(".pop ", mi_lista)


#remove elimina la primera aparición de un elemento específic (entre parentesis) lista

mi_lista = [1,2,3,4,5]
mi_lista.remove(3)
print("remove() ", mi_lista)


#metodo del para eliminar indices concretos que le meta entre los []
del mi_lista[1] #me elimina el segundo elemento de la lista
print("del ", mi_lista)

#len() Devuelve la longitud de una lista Imprime el número de elementos de la lista
print("len() ", len(mi_lista))

#index() devuelve el indice del primer elemento coincidente que le doy entre ()
print(".index() ", mi_lista.index(4))

#count() me imprime cuantas veces aparece un elemento en la lista = sirve para identificar repeticiones
print(".count() ", mi_lista.count(4))

#sort() ordena los elementos de la lista
mi_lista = [3,4,2,1]
mi_lista.sort()
print("sort() ", mi_lista)

#reverse() invierte el orden previo de la kista

mi_lista.reverse()
print("reverse() ", mi_lista)

#slice(): deveulve una porción de la lista = una sublista

sub_lista = mi_lista[1:3] #Creo sublista que incluye el segundo, y tercer elemento ( no el cuarto on posición 3)
print("sub_lista:", sub_lista)

#Listas anidadas
lista_anidada = [[1,2], [3,4], [5,6]]
print("Lista anidada: ", lista_anidada[1][0]) #Sublista con el índice [1] = segunda, primer elemento con índice [0]

#Iteración sobre listas (Loops)
mi_lista = [10, 20, 30, 40]
for elemento in mi_lista:
    print("Loop: ", elemento)

#enumarate() acceder al indice y al valor de cada elemento

mi_lista = ['a', 'b', 'c', 'd']
for index, value in enumerate(mi_lista):
 print(f"Índice: {index}, valor: {value}")
 #enumarate me sirve para que me enumere el valor de un índice concreto en un dataframe muy grande

nombre = "Fernando"
 #print(f"Mi nombre es {nombre}") #así no funcina!!! cuando quiero embedir la variable en el print de un string
 #usar siempre print(f'{}')
print(f'Mi nombre es {nombre}')

#Bucle for para sumar elementos de una lista de números

numeros = [1,2,3,4,5]
suma = 1 #esto le dice desde done partimos en la suma (0), le añado valor cero para que la variable no altere el resultado de la suma de los numeros de la lista

for numero in numeros:
   suma += numero #estamos sumando los números de la lista empezando de cero
print(f'La suma total de la lista es: {suma}')
            
#Otro ejemplo For con sublistas anidadas: iteramos sobre una lista
#que contiene otras listas. Usamos bucle anidado para acceder a cada elemento

lista_anidada = [[1,2], [3,4], [5,6]]
for sub_lista in lista_anidada:
   for elemento in sub_lista:
      #print(elemento) #me printa todos los elementos por separado y en columna de todas las listas y sublistas
    #print(elemento[0][1]) #esto me da error, me tengo que ir a la lista raiz inicial : lista_anidada 
    print(lista_anidada[0][1]) #en cambio, me printa el elemento con índice 1 (segunda) de la primera lista (con índice [0]) 


numeros = [10, 15 ,20,25, 30]
pares = []
impares = []


for numero in numeros:
    if numero % 2 == 0: #si es divisible entre dos e igual a cero
      pares.append(numero) #en la lista "pares" añadele los valores pares de la lista "numeros"
    elif numero % 2 != 0:
      impares.append(numero) #en la lista "impares" añadele los valores pares de la lista "numeros"
      
print(f'Números pares: {pares} y números impares: {impares}')


   
   
