class Rectangle:
    def __init__(self, x, y, h, w):
      '''
Takes x, y coordinates, as well as a width and height, and saves them as instance variables
args: self(class), x(int), y(int), h(int), v(int)
return: None
      '''
      self.x = max(0,x)
      self.y = max(0,y)
      self.height = max(0,h)
      self.width = max(0,w)
    def __str__(self):
      '''
Returns a string containing the x, y, width, and height of the rectangle.
args: self(class)
return: self.width(str)
      '''
      return "(x:"+str(self.x) + ", y=" + str(self.y) +")"+ ", height:" + str(self.height) + ", width:" + str(self.width)

