class Rectangle:
    def __init__(self,length,width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self,v):
        self._length = v
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,v):
        self._length = v
    
    @property
    def perimeter(self):
        return 2 * (self._length + self._width)
    
    @property
    def area(self):
        return self._length * self._width
    
rectangle = Rectangle(4, 5)
rectangle.length = 2
rectangle.width = 3
print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)
