import math
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def cuadrantes(self):
        if self.x >0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
    def vector(self, otro):
        return (otro.x - self.x, otro.y - self.y)
    def distancia(self, otro):
        return math.sqrt((otro.x - self.x)**2 + (otro.y - self.y)**2)