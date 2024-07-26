'''
Operator Overloading
Operator overloading allows you to define how operators (like +, -, *, etc.) behave for objects of your class. This makes your objects interact with each other in a more intuitive and natural way.'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

vector1 = Vector(2, 3)
vector2 = Vector(4, 5)

result = vector1 + vector2
print(result)  # Output: Vector(6, 8)
