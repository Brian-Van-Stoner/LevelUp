class Person():
    
    #constructor method
    def __init__(self, age , height):
        self.age = age
        self.height = height

    #first argument should be self
    def walking (self):
        print("blah blah blah blah")
#creating an obj and calling it human(it name)
human = Person(10,7.5) #call the the class
#Instance of the obj
human.walking() #Invoke the class

