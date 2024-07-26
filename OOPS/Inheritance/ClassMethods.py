
''' Class Methods
A class method is a method that belongs to the class itself, not to any specific object (instance) of the class. It can be used to modify class-level data or perform actions related to the class as a whole. You use the @classmethod decorator to create a class method.'''

class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

# Creating instances of Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("Lucy", 3)

# Changing species using class method
Dog.change_species("Canis lupus familiaris")

print(dog1.species)  # Output: Canis lupus familiaris
print(dog2.species)  # Output: Canis lupus familiaris
