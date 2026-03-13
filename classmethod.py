class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("course:", self.course)


s1 = Student("Prasad", 22, "ECE")
s1.display()