class Object:
    def __init__(self, x, y, pixels=None, char='X'):
        self.x = x
        self.y = y
        self.char = char
        self.pixels = pixels if pixels else []

    def draw(self, renderer):
        for px, py in self.pixels:
            rx = self.x + px
            ry = self.y + py
            if 0 <= rx < renderer.width and 0 <= ry < renderer.height:
                renderer.map[ry][rx] = self.char

    def __repr__(self):
        return f"<Object '{self.char}' at ({self.x},{self.y})>"
    
    def iscollide(self, other):
        self_pix = {(self.x + px, self.y + py) for px, py in self.pixels}
        other_pix = {(other.x + px, other.y + py) for px, py in self.pixels}
        return self_pix.isdisjoint(other_pix)
    
    def rotate(self):
        new_pixels = []
        for px, py in self.pixels:
            new_x = py
            new_y = -px
            new_pixels.append((new_x, new_y))
        min_x = min(x for x, y in new_pixels)
        min_y = min(y for x, y in new_pixels)
        self.pixels = [(x - min_x, y - min_y) for x, y in new_pixels]

class TextObj:
    def __init__(self, x, y, text:str):
        self.x = x
        self.y = y
        self.text = text
    def draw(self, renderer):
        length = len(self.text)
        listtext = list(self.text)
        for i in range(length):
            renderer.map[self.y][self.x + (i)] = listtext[i]
    def __repr__(self):
        return f"<Object '{self.__class__.__name__}' at ({self.x},{self.y})>"
