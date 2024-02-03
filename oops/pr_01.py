class Programmer:
    def __init__(self,name, language,Experience,Projects) :
        self.name=name
        self.language=language
        self.Experience=Experience
        self.Projects=Projects
    def display(self):
        print(f"Name of the programmer is {self.name}.")    
        print(f"language of the programmer is {self.language}.")    
        print(f"Experience of the programmer is {self.Experience}.")    
        print(f"Projects of the programmer is {self.Projects}.")    


for i in range(3):
    name[i]=input("Enter the name of the Programmer")
    language=int(input("Enter the language he know"))
    Experience=int(input("Enter the year of Experience"))
    Project=int(input("Enter the number of Projects he worked on it."))

    name=Programmer(name,language,Experience,Project)

for i in range(3):
    name[i].display()    
# Rupesh=Programmer()
# Amit=Programmer()
# Harikesh=Programmer()       