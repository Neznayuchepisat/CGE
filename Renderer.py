import colorama
import time
import os
import obj
colorama.init(autoreset=True)

class Renderer:
    def __init__(self, width=80, height=40):
        self.width = width
        self.height = height
        self.map = [[' ' for _ in range(width)] for _ in range(height)]
        self.objects = []
    
    def ClearMap(self):
        for y in range(self.height):
            for x in range(self.width):
                self.map[y][x] = ' '

    def DrawOne(self, x, y, type):
        char = 'X' if type == 'fill' else ' '
        self.map[y][x] = char

    def DrawLine(self, x1, y1, x2, y2, type):
        char = 'X' if type == 'fill' else ' '
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.map[y1][x] = char
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.map[y][x1] = char
    
    def AddObject(self, obj):
        self.objects.append(obj)

    def Render(self):
        self.ClearMap()
        os.system('cls' if os.name == 'nt' else 'clear')
        for obj in self.objects:
            obj.draw(self)

        for row in self.map:
            print(''.join(row))

    def RunTest(self):
        while True:
            self.DrawLine(30, 10, 30, 10, 'fill')
            self.Render()
            time.sleep(1)

renderer = Renderer()
renderer.DrawLine(10, 5, 30, 5, 'fill')
renderer.Render()