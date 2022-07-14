#Author: Pablo Escobar
#Carnet: 20936
#Date: 08/07/2022
#Description: Programa generador de archivos BMP 

#Importamos los modulos necesarios
import struct
import numpy as np

# Función que retornara el valor como un objeto de tipo bytes
# con tamano de 1 byte
def char(c):
    #1-byte char
    return struct.pack("=c", c.encode('ascii'))

# Función que retornara el valor como un objeto de tipo bytes
# con tamano de 2 byte
def word(w):
    #2-byte word, little endian
    return struct.pack("=h", w)

# Función que retornara el valor como un objeto de tipo bytes
# con tamano de 4 byte
def dword(d):
    #4-byte dword, little endian
    return struct.pack("=l", d)

# Función que retornara un color como objeto de tipo bytes
def color(r, g, b):
    #1-byte red, 1-byte green, 1-byte blue
    return bytes([int(b * 255), int(g * 255), int(r * 255)])

# Clase para generar el archivo BMP
class Render(object):
    
    # Constructor de la clase
    def __init__(self):
        self.clearColor = color(0,0,0)
        self.viewPortX = 0
        self.viewPortY = 0
        self.viewPortWidth = 0
        self.viewPortHeight = 0
    
    # Función que servira para indicar las dimensiones de la imagen
    # param width: Ancho de la imagen
    # param height: Alto de la imagen	
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()

    # Función que servira para generar el viewPort
    # param x: Posicion en x donde comienza el viewPort
    # param y: Posicion en y donde comienza el viewPort
    # param width: Ancho del viewPort
    # param height: Alto del viewPort
    def glViewPort(self, x, y, width, height):
        self.viewPortX = x
        self.viewPortY = y
        self.viewPortWidth = width
        self.viewPortHeight = height
        self.drawViewPortSquare()

    # Función para dibujar el cuadrado del viewPort
    def drawViewPortSquare(self):
        for x in range(self.viewPortX, self.viewPortX + self.viewPortWidth):
            for y in range(self.viewPortY, self.viewPortY + self.viewPortHeight):
                self.pixels[x][y] = self.currColor
        
        
    # Función para generar el archivo BMP
    # param filename: Nombre del archivo
    def glFinish(self, filename):
        with open(filename, 'wb') as file:

            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))

            # File size
            file.write(dword(14 + 40 + self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(14 + 40))
            
            # Info Header
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
            file.close()
    
    # Función para llenar la matriz de pixeles con el color de fondo
    def glClear(self):
        self.pixels =  [[self.clearColor for y in range(self.height)]
         for x in range(self.width)]

    # Función para llenar la matriz de pixeles con el color indicado
    # param r: Valor de rojo
    # param g: Valor de verde
    # param b: Valor de azul   
    def glClearColor(self, r, g, b):
        self.clearColor = color(r, g, b)
        self.glClear()
    
    # Función para cambiar el color con el que se dibuja
    # param r: Valor de rojo
    # param g: Valor de verde
    # param b: Valor de azul  
    def glColor(self, r, g, b):
        self.currColor = color(r, g, b)
    
    # Función para dibujar un punto en la matriz de pixeles dentro del viewPort
    # param x: Posicion en x donde se dibuja el punto
    # param y: Posicion en y donde se dibuja el punto
    # param clr: Color del punto
    def glPoint(self, x, y, clr = None):
        if( (-1<= x <= 1) and (-1<= y <= 1)):
            xFixed = (x +1) * (self.viewPortWidth // 2) + self.viewPortX
            yFixed = (y +1) * (self.viewPortHeight // 2) + self.viewPortY
            self.pixels[int(xFixed if x<1 else xFixed-1)][int(yFixed if y<1 else yFixed-1)] = clr or self.currColor
            return (xFixed, yFixed)

    def glPointa(self, x, y, clr = None):
        self.pixels[int(x)][int(y)] = clr or self.currColor

    # draw line from (x0, y0) to (x1, y1)
    def drawLine(self,x1,y1,x2,y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        steep = dy > dx
        if steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        offset = 0
        threshold = dx
        y = y1
        for x in np.arange(x1, x2):
            if steep:
                self.glPointa(y, x)
            else:
                self.glPointa(x, y)
            offset += dy * 2
            if offset >= threshold:
                y += 1 if y1 < y2 else -1
                threshold += 2 * dx
        

   
       