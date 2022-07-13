#Author: Pablo Escobar
#Carnet: 20936
#Date: 08/07/2022
#Description: Programa generador de archivos BMP 

# Importamos nuestro modulo para dibujar
import re
import numpy as np
from gl import Render

rend = Render() # Generamos un objeto de tipo Render
rend.glCreateWindow(600, 600) # Creamos una ventana de 512x512
rend.glClearColor(0.01,0.7,0.9) # Establecemos el color de la ventana
rend.glColor(0,0,0) # Establecemos el color del viewPort
rend.glViewPort(25,25,550,550) # Generamos el viewPort

rend.glColor(1,1,1) # Establecemos el color con el que dibujaremos
# rend.glPoint(0,0) # Dibujamos un punto en la posicion (0,0)
puntos = []
cont = 0
for x in np.arange(-1,1,0.1):
    puntos.append(rend.glPoint(x,(x**3)))

for coordenada in range(1,len(puntos)):
        rend.drawLine(puntos[coordenada-1][0],puntos[coordenada-1][1],puntos[coordenada][0],puntos[coordenada][1])

rend.glFinish("output.bmp") # Guardamos el archivo en output.bmp
