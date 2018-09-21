import random

# Create a new class called Agent and add a new function __init__
# We create two new variables, x and y, and give them a random number between 0 and 100
# We also add the environment list into the class (which is defined in the model)
class Agent:
    def __init__ (self,environment,agents):
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)
        self.environment = environment
        self.store = 0
        self.agents = agents
# This step creates a new function called move, where we make each x and y coordinate move
# either +1 or -1 based on a random number        
    def move (self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else: 
            self.y = (self.y - 1) % 100

#This function makes the agents eat the environment around them by 10 if the cooordinates
# are greater than 10
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
    
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
        