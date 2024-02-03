class Student:
    def __init__(self,name,marks,centre) : #Initilising the Constructor
        self.name=name
        self.marks=marks
        self.centre=centre
    def display(self):
        print(f"Name of the Student is {self.name}.")
        print(f"marks of the Student is {self.marks}.")
        print(f"centre of the Student is {self.centre}.")
rupesh=Student("rupesh",89,"California")
rupesh.display()        