class Animal:
    def speak(self):
        return "Animal speaks"

class Bird:
    def fly(self):
        return "Bird flies"

class BirdDog(Animal, Bird):
    pass

# Creating an object of the BirdDog class
birddog = BirdDog()
print(birddog.speak())  # Output: Animal speaks
print(birddog.fly())    # Output: Bird flies
