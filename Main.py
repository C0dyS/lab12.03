class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def print_info(self):
        print(f"student name : {self.name}, age:{self.age}")



student1 = Student('g',20)
student1.print_info()

class Cricle:
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        print(2*3.14*self.radius)

circle_1 = Cricle(10)
circle_1.calculate_area()
