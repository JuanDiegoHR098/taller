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

#5.)Crea una función que reciba la matriz anterior y la pase a un objeto tipo dataframe de Pandas

def dataframe(x):
    return pd.DataFrame(x)

#6.)Crear una función que permita cargar un archivo .mat y .csv  

def cargar_archivo():
    print("1.Cargar archivo .mat\n2.Cargar archivo.csv")
    entrada=int(input("Ingrese una opcion:"))
    if entrada == 1:
        dircc= input("Ingrese la direccion del archivo:")
        return sio.loadmat(dircc)
    elif entrada ==2:
        dircc= input("Ingrese la direccion del archivo:")
        return pd.read_csv(dircc)


#7.Cear funciones de suma, resta, multiplicación, división,logaritmo ,promedio, desviación estándar NOTA:Estas funciones deben permitir hacer estos procesos a lo largo de un eje (usando Numpy) 

def suma(x):
    while True:
        try:
            eje= int(input("Ingresa en que eje desea hacer la suma:"))
            return np.add(x,axis=eje)
        except ValueError:
            print("Error: No se puede hacer la suma en ese eje, ingrese un eje valido")

def resta(x):
    while True:
        try:
            eje= int(input("Ingresa en que eje desea hacer la resta:"))
            return np.subtract(x,axis=eje)
        except ValueError:
            print("Error: No se puede hacer la resta en ese eje, ingrese un eje valido")

def division(x):
    while True:
        try:
            eje= int(input("Ingresa en que eje desea hacer la division:"))
            return np.divide(x,axis=eje)
        except ValueError:
            print("Error: No se puede hacer la division en ese eje, ingrese un eje valido")

def multiplicacion(x):
    while True:
        try:
            eje= int(input("Ingresa en que eje desea hacer la multiplicacion:"))
            return np.multiply(x,axis=eje)
        except ValueError:
            print("Error: No se puede hacer la multiplicacion en ese eje, ingrese un eje valido")

def promedio(x):
    while True:
        try:
            eje= int(input("Ingresa en que eje desea hacer la multiplicacion:"))
            return np.mean(x,axis=eje)
        except ValueError:
            print("Error: No se puede hacer el promedio en ese eje, ingrese un eje valido")

def desviacion_estandar(x):
    while True:
        try:
            eje= int(input("Ingresa en que eje desea hacer la multiplicacion:"))
            return np.nanstd(x,axis=eje)
        except ValueError:
            print("Error: No se puede hacer la desviacion en ese eje, ingrese un eje valido")

#8.) Buscar en Kaggle un archivo .csv relacionadas con alguna patología, descargar y hacer 
# funciones como las propuestas en el ítem anterior, pero implementándolas usando Pandas 
# y que permitan tambien elegir columnas.

def cargar(ruta):
    data= pd.read_csv(ruta)
    return data

def calcular_promedio(data, columna):
    promedio= data[columna].mean()
    return promedio

def filtrar_datos(data, columna, valor):
    datos_filtrados = data[data[columna] > valor]
    return datos_filtrados


def visualizar_grafico(datos, columna_x, columna_y):
    plt.scatter(datos[columna_x], datos[columna_y])
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.title("Gráfico de dispersión")
    plt.show()

m=cargar("Patologias Ray X\pacientesRayosX.csv")
promedio= calcular_promedio(m,"EdadPaciente")
print(promedio)