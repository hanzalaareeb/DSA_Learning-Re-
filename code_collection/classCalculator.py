class Calculator:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def add(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    def div(self):
        if self.y != 0:
            return self.x // self.y
        return self.y // self.x
    def mul(self):
        return self.x * self.y
    def sign(self):
        if self.x > 0 and self.y > 0:
            return "Both numbers are positive"
        elif self.x < 0 and self.y < 0:
            return "Both numbers are negative"
        elif self.x > 0 and self.y < 0:
            return "First number is positive, second is negative"
        elif self.x < 0 and self.y > 0:
            return "First number is negative, second is positive"


clacy = Calculator(7, 2)
print(clacy.div())