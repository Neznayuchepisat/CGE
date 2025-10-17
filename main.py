from Renderer import Renderer
from obj import Object
import time
import inputhandler

pixels_T = [
    (0,0), (1,0), (2, 0),
           (1,1),
           (1,2),
           (1,3)
]

pfirst = [(x-0,0) for x in range(1, 72)]

renderer = Renderer()
inputhand = inputhandler.InputHandler()

obj_T = Object(10, 5, pixels_T, char='R')
linefirst = Object(0, 0, pfirst, char='█')

renderer.AddObject(linefirst)
renderer.AddObject(obj_T)


dx = 1
dy = 1
while True:
    # obj_T.x += dx
    # obj_T.y += dy
    # if obj_T.x > 70 or obj_T.x < 5:
    #     dx *= -1
    # if obj_T.y > 34 or obj_T.y < 1:
    #     dy *= -1
    key = inputhand.get_key()
    if key == 'w':
        obj_T.y -= 1
    elif key == 's':
        obj_T.y += 1
    elif key == 'a':
        obj_T.x -= 1
    elif key == 'd':
        obj_T.x += 1
    elif key == 'q':
        break  
    renderer.Render()

"""Delete this part"""