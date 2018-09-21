# Define a class - person is the name of the class and is a new type of class
# Define a function that will operate within the class that gives the person money and 
# happiness values
class Person:
    def __init__(self, money, happiness):
        self.money = money
        self.happiness = happiness
# This function will change the money and happines values based on whether "work" is 
# assigned to the person     
    def work(self):
        self.money = self.money + 10
        self.happiness = self.happiness - 5
# This function will change the money and happiness based on whether any money is spent        
    def consume(self):
        self.happiness += 7
        self.money -= 8
# This will print the definitions for the self.money and self.happiness function        
    def __repr__(self):
        return (f"A person with money = {self.money} "
                f"and happiness = {self.happiness}")
# Interact with another person which increases both their happiness
    def interact(self, other):
        self.happiness += 1
        other.happiness += 1
        
# Create a variable (person) called Jitse that has a money value of 100
# and a happiness value of 10       
jitse = Person(100, 10)
# Can check the money and happiness values of the person by typing jitse.money in the
# right corner window

# This assignes the work function to Jitse
jitse.work()
# This assignes the consume function to Jitse
jitse.consume()
# This can see how much money Jitse has now he is working
print("Jitse's money:", jitse.money)
# Adding an f in front of the string means curly brackets can be used
print(f"Jitse: money = {jitse.money}, "
      f"happiness = {jitse.happiness}")
print(jitse)

# Create a new person

rob = Person(500, 5)
# Make rob interact with jitse
rob.interact(jitse)
print('After interaction:')
print(jitse)
print(rob)