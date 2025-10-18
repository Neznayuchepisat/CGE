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