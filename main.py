from math import sin
from gl import Render

rend = Render(1024, 512)

rend.glClearColor(0,0.5,0)
rend.glColor(1,1,0)
rend.glClear()

for i in range(512):
    rend.glPoint(i, int(sin(i/10) * 100 + 100))

# rend.glPoint(100,100)
rend.glFinish("output.bmp")