#3 attributes and 2 methods
class Dog:
    
    def __init__(self, name, speed, breed):
        self.name = name
        self.speed = speed 
        self.breed = breed  

    def bark(self):
        return f"My dogs name is {self.name}, he is a {self.breed}"

    def running(self):
        return f"A {self.breed} can run at upto {self.speed}"
        
