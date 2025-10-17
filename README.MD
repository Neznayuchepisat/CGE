# Console Game Engine
CGE it's a simple console game engine. It's very weak, but it does have some functionality.

## how it works?
It works very easy:

### obj.py
obj.py is simply an object class in which all objects and their methods are defined.

### Renderer.py
This is a graphics engine class.

1. DrawOne:
DrawOne() it's a method for fill ONLY 1 pixel in the console
example: 
DrawOne(5, 5, fill) - fill pixel
DrawOne(5, 5, erase) - Erase pixel

2. DrawLine:
DrawLine() it's a method for fill Line of pixels
example:
renderer.DrawLine(10, 5, 30, 5, 'fill')

3. Render:
Render() need for render console. It can render ONLY 1 frame or a lot of frames.
example:
renderer = Renderer()
renderer.DrawLine(10, 5, 30, 5, 'fill')
renderer.Render()

### inputhandler.py
This is a file for processing keys.

1. _captureinput:
starts a parallel process

2. _get_key:
determines whether a key is pressed and which one

3. get_key
variable storing the last key

### main.py
it's a file for the main logic. This is where you write your code.