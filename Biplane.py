class Airplane:

    vehicle = "Flying machine"

    def __init__(self, wingspan=0, model="", passenger_cap=0, location=""):
        self.wingspan = wingspan
        self.__model = model
        self._passenger_cap = passenger_cap
        self.location = location

    def __str__(self):
        return "The wingspan of the plane is " + str(self.wingspan) + ". The model is " + self.__model + ". The location is " + str(self.location)

    def fly_airplane(self, new_loc):
        self.location = new_loc


    def get_wingspan(self):
        return self.wingspan

    def set_wingspan(self, new_wingspan):
        self.wingspan = new_wingspan

    def get_model(self):
        return self.__model

    def set_model(self, new_wingspan):
        self.__model = new_wingspan


class Biplane(Airplane):
    def __init__(self, wingspan=0, model="", passenger_cap=0, location="", wings=2):
        super().__init__(wingspan, model, passenger_cap, location)
        self.wings = wings

    def num_wings(self):
        print(self.wings)
        print("Do a loop dee loop")

    def fly_airplane(self, new_loc):
        self.location = new_loc
        print(self.location, "this is the overrided method")

biplane = Biplane(35)
biplane.num_wings()
biplane.fly_airplane("Chicago")

airplane = Airplane()
airplane.fly_airplane("Washington DC")
print(airplane.location)

print(issubclass(Airplane, Biplane))
