#create a class and give it 4 attribute and 2 methods
class Car:
    
    def __init__(self, brand, color, mileage, seats):
        self.brand = brand
        self.color = color 
        self.mileage = mileage
        self.seats = seats 

    def car_mileage(self):
        return f"The {self.color} {self.brand} with {self.seats} has a mileage of {self.mileage}"

    def running(self): 
        return f"Majority of {self.brand} cars are {self.color} in color and have an average of {self.mileage} per year"
    