#Intitate a class
class employee:
    #special method/ magic method
    def __init__(self): 
        print(id(self))
        # print("Starting exceuting attributes/data")
        # print("Starting exceuting attributes/data")
        self.id = 123
        self.salary= 50000
        self.dep = "DATA SCIENCE"
        # print("Starting exceuting attributes/data")
    
    def travel(self):
        print("This travel method was called manually")
        print(f"Employee is traveling to Delhi")





#Create an obj/instance of the class
sam = employee()
sam.name= "Sam kumar"
print(sam.name)
# shaktiman=employee()
# print(id(shaktiman))
# print(id(sam))
# sam.travel()
# print(sam.id)


 