import pandas as pd

# This CSV file contains semicolons instead of comas as separator
df = pd.read_csv('assets/real_estate.csv', sep=';')
print(df)

import pandas as pd
import numpy as np

highest_price = df['price'].max() #esto busca el valor más alto del level "price" en todo el csv
print(highest_price)

highest_price_row = df.loc[df['price'] == highest_price] #Del highest_price printar toda la fila o row con el highest_price 
'''highest_price_row es toda la información de la fila con el precio más alto
el ds.loc de precio debe ser = a precio mas alto, 
.loc siempre trae la fila, .loc = me imprime el valor o contenido.'''

print(highest_price_row) #me imprime toda la información de la fila con el precio más alto

house_address_high = highest_price_row['address'].values[0] #.values porque la fila me trae una serie de valores que si son correctos, 
#el codigo reconoce que la lista tiene toda la info de la fila
#con el [0] le digo que se pare en el primer valor que es el primer valor que cumple con condición del precio 
#.values[] me traer el contenido de la dirección en forma de texto

print(house_address_high)

print(f'The house with address {house_address_high} is the most expensive and its price is {highest_price} USD')


#Ejercicio 2

import pandas as pd
import numpy as np

#Paso 1) Filtrar ceros
filtered_df = df[df['price'] > 0]

print(filtered_df)

#Paso 2) Crear variable con el precio mínimo (ya habiendo excluido precios = cero)
lowest_price = filtered_df['price'].min()

print(lowest_price)

#Paso 3) Recuperar todo el contenido/valores (Sólo el contenido, no labels de columnas) de la fila con el precio más bajo
lowest_price_row = df.loc[df['price'] == lowest_price] #Del lowest_price printa todo el contenido de la fila o row con el highest_price 
prices = df.loc[df['price']] #Variable que contiene todos los valores bajo le columna con label 'price'
'''Ojo esto está mal!!!: prices = df.loc['price']'''
print(prices)

'''highest_price_row es toda la información de la fila con el precio más alto
el ds.loc de precio debe ser = a precio mas alto, 
.loc siempre trae la fila, .loc = me imprime el valor o contenido.'''

print(lowest_price_row) #me imprime sola la información o contenido de la fila con el precio más bajo
 
#Paso 4) Crear variable con sólo la dirección de la fila con el precio más bajo
house_address_low = lowest_price_row['address'].values[0] #.values porque la fila me trae una serie de valores que si son correctos, 
#el codigo reconoce que la lista tiene toda la info de la fila
#con el [0] le digo que se pare en el primer valor que es el primer valor que cumple con condición del precio 
#.values[] me traer el contenido de la dirección en forma de texto


#Paso 5) Frase con las variables definidas antes
print(f'The house with address {house_address_low} is the cheapest and its price is {lowest_price} USD')


# See https://stackoverflow.com/questions/62878893/finding-the-minimum-value-above-0-in-a-2d-array-python 


#otra forma mas corta

df['price'] = pd.to_numeric(df['price'], errors = 'coerce')
prices_list = df[df['price'] > 0]
cheapest_row = df.loc[prices_list['price'].idxmin()]
    