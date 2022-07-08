import struct

def char(c):
    #1-byte char
    return struct.pack("=c", c.encode('ascii'))

def word(w):
    #2-byte word, little endian
    return struct.pack("=h", w)

def dword(d):
    #4-byte dword, little endian
    return struct.pack("=l", d)

def color(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])

class Render(object):
    def __init__(self,width,height):
        self.width = width 
        self.height = height
        self.clearColor = color(0,0,0)

        self.glClear()

    def glFinish(self, filename):
        with open(filename, 'wb') as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))

            # File size
            file.write(dword(14 + 40 + self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(14 + 40))
            #Info Header
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
        

            



    

    def glClear(self):
        self.pixels =  [[self.clearColor for y in range(self.height)]
         for x in range(self.width)]
        
    def glClearColor(self, r, g, b):
        self.clearColor = color(r, g, b)
        self.glClear()
    
    def glColor(self, r, g, b):
        self.currColor = color(r, g, b)
    
    def glPoint(self, x, y, clr = None):
        if( 0<= x < self.width and 0 <= y < self.height):
            self.pixels[x][y] = clr or self.currColor


    def render(self, string):
        self.buffer.extend(string)

    def __str__(self):
        return str(self.buffer)