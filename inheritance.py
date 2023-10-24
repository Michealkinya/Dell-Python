#This is my parent class
class animal:

    def speak(self):
        print("Animal is speaking")


class dog(animal):
    def bark(self):
        print("Dog is barking")

class cat(animal):
    def meow(self):
        print("Cat is meowing")

d = dog()
d.speak()

c = cat()
c.meow()