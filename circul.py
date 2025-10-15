from math import pi

class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * radius
        self._area = pi * radius ** 2
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def diameter(self):
        return self._diameter
    
    @property
    def area(self):
        return self._area
    
circle = Circle(1)

print(circle.radius)
print(circle.diameter)
print(circle.area)
