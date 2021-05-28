class Student:
    school = "AkiraChix"
    def __init__(self, name, age, read):#Creating an instance of a class in python
        self.name = name
        self.age = age   
        self.read = read

    def speak(self):
        return f"Hello my name is {self.name}, I am {self.age} years old and I love {self.school}."

    def book(self):
        return f"Hi, I'm {self.name}, currently reading a book called {self.read}"
