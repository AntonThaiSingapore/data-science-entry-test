#q7
#Task 1:

class Car:
    #assign values to Car_object properties
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    #print information about the car as "Year Make Model"
    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

#Task 2:
car1 = Car("Toyota", "Corolla", 2020)
car1.describe_car()
