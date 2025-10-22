class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        return f"The {self.brand} is driving at {self.speed}"
    
    def boost(self):
        return f"Boost activated! Speed is now {self.speed + 20} km/h."
    
c = Car("Toyota", 100)
print(c.drive())
print(c.boost())