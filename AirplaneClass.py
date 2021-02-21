class Airplane:

    def __init__(self, wingspan, model, passenger_cap, location, fuel):
        self.wingspan = wingspan
        self.model = model
        self.passenger_cap = passenger_cap
        self.location = location
        self.fuel = fuel

    def __str__(self):
        return "The wingspan of the plane is " + str(self.wingspan) + ". The model is " + self.model + ". The location is " + str(self.location)

    def fly_airplane(self, new_loc):
        self.location = new_loc
        self.fuel = self.fuel * 0.5

    def get_wingspan(self):
        return self.wingspan


    def set_wingspan(self, new_wingspan):
        self.wingspan = new_wingspan

"""plane1 = Airplane()

plane1.wingspan = 100
plane1.model = "Boeing 737"
plane1.passenger_cap = 150
plane1.location = "Chicago"
plane1.fuel = 2000"""

plane2 = Airplane(150, "Airbus A330", 350, "London", 3500)
print(plane2)

"""plane2.set_wingspan(125)
print(plane2.get_wingspan())

#plane1.fly_airplane("New York")
plane2.fly_airplane("Los Angeles")"""

print(plane2.fuel)
print(plane2.location)
