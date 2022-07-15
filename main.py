#Author: Pablo Escobar
#Carnet: 20936
#Date: 08/07/2022
#Description: Programa generador de archivos BMP 

# Importamos nuestro modulo para dibujar
from gl import Render
from gl import color
import numpy as np
def drawLineFromArray(puntosFigura):
    for coordenada in range(1,len(puntosFigura)):
        rend.drawLine(puntosFigura[coordenada-1][0],puntosFigura[coordenada-1][1],puntosFigura[coordenada][0],puntosFigura[coordenada][1])
    rend.drawLine(puntosFigura[0][0],puntosFigura[0][1],puntosFigura[len(puntosFigura)-1][0],puntosFigura[len(puntosFigura)-1][1])



rend = Render() # Generamos un objeto de tipo Render
rend.glCreateWindow(600, 600) # Creamos una ventana de 512x512
rend.glClearColor(0.01,0.7,0.9) # Establecemos el color de la ventana
rend.glColor(0,0,0) # Establecemos el color del viewPort
rend.glViewPort(25,25,550,550) # Generamos el viewPort

rend.glColor(1,1,1) # Establecemos el color con el que dibujaremos
# rend.glPoint(0,0) # Dibujamos un punto en la posicion (0,0)
# puntos = []
# cont = 0
# for x in np.arange(-1,1.1,0.1):
#     puntos.append(rend.glPoint(x,(x**3)))


puntosFigura1 = [rend.glPoint(-0.6,0.6), rend.glPoint(-0.2,0.6), rend.glPoint(-0.2,0.2), rend.glPoint(-0.6,0.2)]
drawLineFromArray(puntosFigura1)

puntosFigura2 = [rend.glPoint(0,0.2), rend.glPoint(0.5,0.2), rend.glPoint(0.25,0.6)]
drawLineFromArray(puntosFigura2)

puntosFigura3 = [rend.glPoint(-0.5,-0.4), rend.glPoint(0.6,-0.4), rend.glPoint(0.6,0)]
drawLineFromArray(puntosFigura3)

puntosFigura4 = [rend.glPoint(-0.6,-0.8),rend.glPoint(0.6,-0.8),rend.glPoint(0.6,-0.9),rend.glPoint(-0.6,-0.9)]
drawLineFromArray(puntosFigura4)

puntosFigura5 = [rend.glPoint(-0.2,-0.5),rend.glPoint(0.2,-0.5),rend.glPoint(0.4,-0.6),rend.glPoint(0.2,-0.7),rend.glPoint(-0.2,-0.7),rend.glPoint(-0.4,-0.6)]
drawLineFromArray(puntosFigura5)


#EXTRA decagono
puntosFigura6 = []
for i in range(0,10):
    puntosFigura6.append(rend.glPoint(0.1*np.cos(i*2*np.pi/10),0.1*np.sin(i*2*np.pi/10)))

drawLineFromArray(puntosFigura6)

# Extra pintar poligono dado coordenadas x,y
rend.fillPolygon(puntosFigura5)


rend.glFinish("output.bmp") # Guardamos el archivo en output.bmp
