
class Test: 

    def __init__(self, name, age = 0):
        if(type(age) not in(int, float)):
            raise Exception('Args not numbers')
        self.name = name 
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self): 
        return self.age

    def printPerson(self): 
        print(
            'Name: ' , self.name, "\n"
            'Age: ', self.age
        )


t = Test('Khalid',22)

t.printPerson()
