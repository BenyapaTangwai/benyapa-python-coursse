class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"Woof! I'm {self.name} and I'm {self.age} years old."
    
my_dog = Dog("Ben", 19)
print(my_dog.bark())