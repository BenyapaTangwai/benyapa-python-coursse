"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self, length, width):
        self.__length = length #private โดยเพิ่ม __
        self.__width = width #private โดยเพิ่ม __

    # Method to get the area
    def getArea(self):
        area = self.__length * self.__width
        return f"Area = {area}"

    # Method to get the perimeter
    def getPerimeter(self):
        perimeter = (self.__length + self.__width) * 2
        return f"Perimeter = {perimeter}"
    
    def isSquare(self):
        if self.__length == self.__width :
            return f"it's a square"
        else:
            return f"if's a rectangle"

rect = Rectangle(10, 5)
print(rect.getArea())       # print Area = 50
print(rect.getPerimeter())  # print Perimeter = 30
print(rect.isSquare())      # print True/False