from Rectangle import Rectangle

class Surface:
    def __init__(self, filename, x, y, h, w):
      '''
Takes a x, y set of coordinates, as well as a width and height, and creates a rectangle object stored in self.rect
Args: self(class), filename, x(int), y(int), h(int), w(int)
Return: None
      '''
      self.image = filename
      self.rect = Rectangle(x, y, h, w)

    def getRect(self):
      '''
returns the rectangle object
Args: self(class)
Return: self.rect(object)
      '''
      return self.rect
