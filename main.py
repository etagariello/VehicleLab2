class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        print("A vehicle has been made.")

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight}")

    def horn(self):
        print("HONK")

class Car(Vehicle):
    def __init__(self, make, method, year, weight, num_doors):
        super().__init__(make, method, year, weight)
        self.num_doors = num_doors
        print("It was a car!")

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight}\nNumber of doors: {self.num_doors}")

    def horn(self):
        print("BEEP BEEP!")


aCar = Car("BMW", "I8", 2023, 2000, 4)
aCar.display_info()
aCar.horn()

class Truck(Vehicle):
    def __init__(self, make, method, year, weight, payload_capacity):
        super().__init__(make, method, year, weight)
        self.payload_capacity = payload_capacity
        print("It was a truck!")

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight}\nPayload capacity: {self.payload_capacity}")

    def horn(self):
        print("HONK HONK!")

    def dump(self):
        print("Load has been dumped!")

aTruck = Truck("Honda", "Thick", 2023, 5000, 3000)
aTruck.display_info()
aTruck.horn()
aTruck.dump()

class Boat(Vehicle):
    def __init__(self, make, method, year, weight, boat_type):
        super().__init__(make, method, year, weight)
        self.boat_type = boat_type
        print("It was a boat!")

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight}\nBoat type: {self.boat_type}")

    def horn(self):
        print("TOOT TOOT!")

    def anchor(self):
        print("The anchor has been dropped!")

aBoat = Boat("Betty", "Gorno", 2023, 1500, "Sailboat")
aBoat.display_info()
aBoat.horn()
aBoat.anchor()