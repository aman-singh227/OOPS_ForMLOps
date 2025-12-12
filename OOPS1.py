#Intitate a class
class employee:
    #special method/ magic method
    def __init__(self): 
        print("Starting exceuting attributes/data")
        self.id = 123
        self.salary= 50000
        self.dep = "DATA SCIENCE"
        print("Starting exceuting attributes/data")
    
    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Employee is traveling to {destination}")





#Create an obj/instance of the class
sam = employee()

# print(sam.id)


