class Shape:
    def __init__(self, n) -> None:
        self.n = n
        
    
    def area(self):
        pi = 3.14
        if self.n == 1:
            return pi * (self.r ** 2)
        elif self.n == 2:
            return self.l * self.w
        elif self.n == 3:
            return 0.5 * self.b * self.h
        
    def parameter(self):
        pi = 3.14
        if self.n == 1:
            return pi * (self.r) * 2
        elif self.n == 2:
            return 2 * (self.l + self.w)
        elif self.n == 3:
            return "Not enough Info."
        
class Circle(Shape):
    def __init__(self, r):
        super().__init__(1)
        self.r = r
class Quadr(Shape):
    def __init__(self, l, w):
        super().__init__(2)
        self.l = l
        self.w = w
class Triangle(Shape):
    def __init__(self, b, h) -> None:
        super().__init__(3)
        self.b = b
        self.h = h
circle = Circle(4)
print(circle.area())
print(circle.parameter())
quad = Quadr(2, 2)
print(quad.area())
print(quad.parameter())

triangle = Triangle(2, 4)
print(triangle.area())
print(triangle.parameter())