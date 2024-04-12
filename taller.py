import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io as sio


#1-)Crear una matriz de Numpy aleatoria de 4 dimensiones y un size de 1200000 

y= np.random.random((30,40,10,100))


#2-) Crea una copia de la matriz creada en el ítem anterior (usar método copy) de solo 3 
# dimensiones (“Cortando una de las dimensiones”) 

q= y[:,:,:,10].copy()
print()


# 3. De la matriz 3D, muestra todos los atributos propios de dicha matriz , dimensión, tamaño, 
# etc..

w=q.shape
e=q.size
r= q.dtype
t= q.ndim


#4.) Modificar su forma y pasarla a 2D

u= q.reshape(40,300)
print(u)

