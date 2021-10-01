class Student:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def printInfo(self):
        print("The student's name is:",self.name)
        print("The student is studying:",self.subject)


studentOne = Student("Peter", "Software Engineering")

studentOne.printInfo()



