import random
import operator
import matplotlib.pyplot

# Set a function that takes two arbitrary agents and returns distant between them
# Agent row a is the first agent we want to look at, and agent row b is the second
# the number in square brackets i.e. 0 or 1 refers to the first or second value in the 
# agent. I.e. the x or y value
def distance_between(agents_row_a, agents_row_b):
    answer = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    return answer
# Set the number of agents to 10
num_of_agents = 10

# This will eventually make a loop that runs 100 times
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

# Calling on this function calculates the distance between all of the points
# in all of the agents
# But, this will test each agent against itself, as well as against the other
# agents more than once 
for agents_row_a in agents:
        for agents_row_b in agents:
            distance = distance_between(agents_row_a, agents_row_b)
            
# To fix this, we can set a new loop where each agent will be tested only
# against the agents below it in the list, therefore avoiding duplictaes and
# tests against self
for x in range(num_of_agents):
    for z in range(x + 1,num_of_agents):
        distance = distance_between(agents[x], agents[z])
        print(distance)