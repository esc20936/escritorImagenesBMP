#Author: Pablo Escobar
#Carnet: 20936
#Date: 08/07/2022
#Description: Programa generador de archivos BMP 

# Importamos nuestro modulo para dibujar
from gl import Render

rend = Render() # Generamos un objeto de tipo Render
rend.glCreateWindow(512, 512) # Creamos una ventana de 512x512
rend.glClearColor(0.01,0.7,0.9) # Establecemos el color de la ventana
rend.glColor(0.8,0.8,0.8) # Establecemos el color del viewPort
rend.glViewPort(4,4,500,500) # Generamos el viewPort

rend.glColor(1,0,0) # Establecemos el color con el que dibujaremos
rend.glPoint(0,0) # Dibujamos un punto en la posicion (0,0)

rend.glFinish("output.bmp") # Guardamos el archivo en output.bmp
