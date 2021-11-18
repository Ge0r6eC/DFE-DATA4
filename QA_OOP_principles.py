
from abc import ABC, abstractmethod

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "squark"

    def reproduce(self):
        self.babies += 1
        return self.babies
    
    @abstractmethod
    def eat(self):
        pass

    extinct = False

class Owl(Bird):
    
    def reproduce(self):
        self.babies += 6
        return self.babies

    def eat(self):
        return "Peck Peck"


tawnyOwl = Owl()

print(tawnyOwl.eat())
print(tawnyOwl.reproduce())
print(tawnyOwl.noise())

print(tawnyOwl.fly)



