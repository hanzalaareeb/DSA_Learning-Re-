class Circle:
    """def __init__(self, r) -> None:
        self.r = r"""
        
    def area(self, r):
        return 3.14 * (r ** 2)
    

newCircle = Circle()
area = newCircle.area(1)
print(area)