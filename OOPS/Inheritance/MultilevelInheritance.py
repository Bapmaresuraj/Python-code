class Animal:
    def speak(self):
        return "Animal speaks"

class Mammal(Animal):
    def walk(self):
        return "Mammal walks"

class Dog(Mammal):
    def bark(self):
        return "Dog barks"

# Creating an object of the Dog class
dog = Dog()
print(dog.speak())  # Output: Animal speaks
print(dog.walk())   # Output: Mammal walks
print(dog.bark())   # Output: Dog barks
