'''Property Decorators
Property decorators make methods behave like attributes. They help you define getter, setter, and deleter methods in a clean and readable way.

@property
The @property decorator allows you to access a method like an attribute.'''

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

circle = Circle(10)
print(circle.radius)  # Output: 10

'''@.getters and @.setters
With @property, you can control how you get and set an attribute's value. This is useful for validation or modifying the behavior when the attribute is accessed or changed.'''

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

circle = Circle(10)
print(circle.radius)  # Output: 10

circle.radius = 15
print(circle.radius)  # Output: 15

# Trying to set a negative radius will raise an error
# circle.radius = -5  # Raises ValueError: Radius cannot be negative
