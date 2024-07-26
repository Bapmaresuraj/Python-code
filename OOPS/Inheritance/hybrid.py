class Animal:
    def speak(self):
        return "Animal speaks"

class Mammal(Animal):
    def walk(self):
        return "Mammal walks"

class Bird(Animal):
    def fly(self):
        return "Bird flies"

class Bat(Mammal, Bird):
    pass

# Creating an object of the Bat class
bat = Bat()
print(bat.speak())  # Output: Animal speaks
print(bat.walk())   # Output: Mammal walks
print(bat.fly())    # Output: Bird flies
