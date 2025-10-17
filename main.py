from Renderer import Renderer
from obj import Object
import time

pixels_T = [
    (0,0), (1,0), (2, 0),
           (1,1),
           (1,2),
           (1,3)
]

pixels_block = [
    (0,0), (1,0),
    (0,1), (1,1)
]

renderer = Renderer()

obj_T = Object(10, 5, pixels_T, char='R')
obj_block = Object(20, 10, pixels_block, char='O')

renderer.AddObject(obj_T)
renderer.AddObject(obj_block)

dx = 1
while True:
    obj_T.x += dx
    if obj_T.x > 70 or obj_T.x < 5:
        dx *= -1
    renderer.Render()
    time.sleep(0.05)
