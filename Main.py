class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def print_info(self):
        print(f"student name : {self.name}, age:{self.age}")



student1 = Student('g',20)
student1.print_info()